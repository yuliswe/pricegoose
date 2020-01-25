
from tests.integration import IntegrationTestCase

from lib.ipromise import augments
from src.common.models import Category, Product


class TestBasketAndOrder(IntegrationTestCase):

    @augments(IntegrationTestCase)
    def setUp(self):
        cat = Category.objects.create(id=1, name='testcategory')
        prod = Product.objects.create(name_en='testprod', name_zh='测试商品')
        cat.products.add(prod)
