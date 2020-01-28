from django.urls import resolve
from django.views import generic


class BaseView(generic.View):
    def context(self, request=None):
        if not request:
            request = self.request
        context = {}
        context.update({
            'site_logo': 'PriceGoose',
            'site_title': 'Track Lowest Price for Fashion & Electronics',
            'app_js_url': resolve(self.request.path).namespaces[-1] + '.js',
        })
        return context
