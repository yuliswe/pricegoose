import { id, DEEP, URLs, SHALLOW, ObjectAPI } from './base'

export interface Category<D>
{
    id: id
    name: string
}

export class CategoryAPI extends ObjectAPI<Category<SHALLOW>, Category<DEEP>>
{
    public readonly URL:string = URLs.CATEGORY
}
