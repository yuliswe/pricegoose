import { id, DEEP, URLs, SHALLOW, ObjectAPI } from './base'
import { BasketProduct } from './basket_product'

export class SessionBasketProductAPI extends ObjectAPI<BasketProduct<SHALLOW>, BasketProduct<DEEP>>
{
    public readonly URL: string = URLs.SESSION_BASKET_PRODUCT
}
