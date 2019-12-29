from django.urls import resolve
from django.views import generic


class BaseView(generic.View):
    def context(self, request=None):
        if not request:
            request = self.request
        context = {}
        context.update({
            'app_js_url': f'webpack/{resolve(request.path).app_name}.js'
        })
        return context
