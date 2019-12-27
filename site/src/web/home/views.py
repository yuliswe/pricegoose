from django.shortcuts import render
from src.web.base.views import BaseView
from ipromise import overrides


class IndexView(BaseView):
    def get(self, request):
        return render(request, 'home/html/trend.html', self.context())
