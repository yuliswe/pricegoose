from django.shortcuts import render
from src.web.base.views import BaseView
from ipromise import overrides


class TrendsView(BaseView):
    def get(self, request):
        return render(request, 'home/trends/tmpl.html', self.context())
