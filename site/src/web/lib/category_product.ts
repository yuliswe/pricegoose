import { id, DEEP, SHALLOW, ObjectAPI, URLs } from './base'
import { Product } from './product'
import { Category } from './category'

export interface ProductCategory<D> {
    id: id
    product: D extends DEEP ? Product<SHALLOW> : id
    category: D extends DEEP ? Category<SHALLOW> : id
}

type ProductCategoryShallow = SHALLOW extends DEEP ? number : id

export class ProductCategoryAPI extends ObjectAPI<ProductCategory<SHALLOW>, ProductCategory<DEEP>>
{
    public readonly URL: string = URLs.CATEGORY_PRODUCT
}
