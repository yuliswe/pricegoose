import { id, int, DEEP, SHALLOW, URLs, ObjectAPI } from './base'
import { ProductImage } from './product_image'
import { Category } from './category'

export interface Product<D> {
    id: id
    images: D extends DEEP ? ProductImage<SHALLOW>[] : id[]
    categories: D extends DEEP ? Category<SHALLOW>[] : id[]
    name_zh: string
    name_en: string
    description: string
    brand_en: string
    brand_zh: string
    weight_g: number
    weight_oz: number
    volume_ml: number
    volume_oz: number
    description_md: string
    barcode: string
    base_price: string
    leftover: int
    date_created: string
    date_modified: string
    parent: null
}

export class ProductAPI extends ObjectAPI<Product<SHALLOW>, Product<DEEP>>
{
    public readonly URL = URLs.PRODUCT
}
