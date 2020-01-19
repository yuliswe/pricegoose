import { id, DEEP, SHALLOW, ObjectAPI, URLs } from './base'
import { Product } from './product'

export interface BasketProduct<D> {
    id: id
    product: D extends DEEP ? Product<SHALLOW> : id
    quantity: number
}

export class BasketProductAPI extends ObjectAPI<BasketProduct<SHALLOW>, BasketProduct<DEEP>>
{
    public readonly URL: string = URLs.BASKET_PRODUCT
}
