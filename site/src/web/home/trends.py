from django.shortcuts import render
from src.web.base.views import BaseView
from ipromise import overrides

from src.web.home.tags.price_drop_carousel import ProductWithPriceDropInfo


class TrendsView(BaseView):
    def get(self, request):
        return render(request, 'home/trends.html', self.context())

    @overrides(BaseView)
    def context(self):
        context = super().context()
        context.update({
            'fashion_pd_list': [
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
            ],
            'electronics_pd_list': [
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
                ProductWithPriceDropInfo(),
            ]
        })
        return context
