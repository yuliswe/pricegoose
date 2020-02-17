from django.core.exceptions import FieldError
from ipromise import overrides
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)

from src.common import models as m
# from src.common import serializers as s
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class ApiPagination(PageNumberPagination):
    page_query_param = '_page'
    page_size_query_param = '_limit'
    page_size = 50
    max_page_size = 100

    @overrides(PageNumberPagination)
    def get_paginated_response(self, data):
        return Response({
            'page': self.page.number,
            'limit': self.get_page_size(self.request),
            'total': self.page.paginator.count,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'objects': data,
        })


class BaseModelAPI(GenericAPIView):
    """ base class for requests to /products or /products/1 """
    pagination_class = ApiPagination

    __model_serializers = {
    }

    __model_names = {
    }

    def get_model_serializer(self, model):
        if model in self.__model_serializers:
            return self.__model_serializers[model]
        else:
            raise NotImplementedError(f'Model {model} not found in BaseModelAPI.__model_serializers. Did you forget to add?')

    def _filter_queryset(self, queryset):
        querydict = {}
        for key in self.request.query_params:
            if '[]' in key:
                querydict[key.replace('[]', '')] = self.request.query_params.getlist(key)
            else:
                querydict[key] = self.request.query_params.get(key)
        if '_limit' in querydict:
            del querydict['_limit']
        if '_page' in querydict:
            del querydict['_page']
        try:
            return queryset.filter(**querydict).order_by('pk')
        except FieldError as e:
            raise ValidationError(e)

    @property
    def model(self):
        model_name = self.kwargs['model']
        if model_name not in self.__model_names:
            raise NotImplementedError(f'Model {model_name} not found in BaseModelAPI.__model_names. Did you forget to add?')
        return self.__model_names[model_name]

    @overrides(GenericAPIView)
    def get_serializer_class(self):
        return self.get_model_serializer(self.model)

    @overrides(GenericAPIView)
    def get_queryset(self, *args, **kwargs):
        return self._filter_queryset(self.model.objects.all())


class ModelAPI(ListCreateAPIView, BaseModelAPI):
    """ handle request such as GET/POST /products """
    pass


class ModelObjectAPI(RetrieveUpdateDestroyAPIView, BaseModelAPI):
    """ handle requests such as GET/DELETE/PATCH /products/1 """
    pass


class ModelFieldAPI(mixins.ListModelMixin, mixins.RetrieveModelMixin, BaseModelAPI):
    """ handle requests such as GET/POST/PUT /products/1/images """

    def get(self, request, *args, **kwargs):
        result = getattr(self.model_object, self.field_name)
        if isinstance(result, m.Model):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def request_body_as_json(self):
        data = self.request.data
        if not (isinstance(data, int) or
                (isinstance(data, list) and
                    (len(data) == 0 or
                     (len(data) > 0 and isinstance(data[0], int))))):
            raise ValidationError(f'Expected ids in the request body, but got {data} instead')
        return data

    def post(self, request, *args, **kwargs):
        pk = self.request_body_as_json()
        getattr(self.model_object, self.field_name).add(pk)
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        pk_list = self.request_body_as_json()
        getattr(self.model_object, self.field_name).set(pk_list)
        return self.get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pk = self.request_body_as_json()
        getattr(self.model_object, self.field_name).remove(pk)
        return self.get(request, *args, **kwargs)

    @property
    def field_name(self):
        field_name = self.kwargs['target_field']
        if not hasattr(self, '__field_name_checked'):
            self.__field_name_checked = True
            if not hasattr(self.model, field_name):
                raise ValidationError(f'{self.model.__name__} does not have property {field_name}')
            target_field = self.model._meta.get_field(field_name)
            if not any([isinstance(target_field, ty) for ty in [
                m.ForeignKey, m.ManyToManyRel, m.ManyToOneRel
            ]]):
                raise ValidationError(f'property {field_name} on {self.model.__name__} is not a relation')
        return field_name

    @property
    def model_field_instance(self):
        return getattr(self.model_object, self.field_name)

    @property
    def field_model(self):
        return self.model._meta.get_field(self.field_name).related_model

    @property
    def model_object(self):
        pk = self.kwargs[self.lookup_field]
        return get_object_or_404(self.model, pk=pk)

    @overrides(GenericAPIView)
    def get_serializer_class(self):
        return self.get_model_serializer(self.field_model)

    @overrides(GenericAPIView)
    def get_queryset(self, *args, **kwargs):
        result = getattr(self.model_object, self.field_name)
        if result is None:
            return m.QuerySet(model=self.model)
        # if isinstance(result, m.Model):
        #     return self._filter_queryset(self.field_model.objects.filter(pk=result.pk))
        return self._filter_queryset(getattr(self.model_object, self.field_name).all())

    @overrides(GenericAPIView)
    def get_object(self, *args, **kwargs):
        return getattr(self.model_object, self.field_name)
