from django.urls import resolve
from django.views import generic


class BaseView(generic.View):
    def context(self):
        context = {}
        context.update({
            'app_js_url': f'webpack/{resolve(self.request.path).app_name}.js'
        })
        return context
