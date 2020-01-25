import { id, DEEP, SHALLOW, ObjectAPI, URLs } from './base'
import { Product } from './product'

export interface ProductImage<D> {
    id: id
    product: D extends DEEP ? Product<SHALLOW> : id
    url: string
}

export class ProductImageAPI extends ObjectAPI<ProductImage<SHALLOW>, ProductImage<DEEP>>
{
    public readonly URL: string = URLs.PRODUCT_IMAGE
}
