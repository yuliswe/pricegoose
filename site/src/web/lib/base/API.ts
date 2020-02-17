import {Model, ModelConstructor, Collection} from './Model'
import {id, int} from './base'
import {AjaxDriver} from './base'
import {jqueryAjaxDriver} from './jqueryAjaxDriver'

export type PageQuery<T extends Model> = {
    page?: int
    limit?: int
}

export type GetQuery<T extends Model> = {
    [K in keyof T]?: (T[K] extends (number | string | boolean) ? T[K] : id)
}

export interface DeleteQuery {
    id: id
}

export type CreateQuery<T extends Model> = {
    [K in keyof T]?: (T[K] extends (number | string | boolean) ? T[K] : id)
}
export type UpdateQuery<T extends Model> = CreateQuery<T> & {id: id}


export class API<T extends Model> {

    readonly _ajax_driver: AjaxDriver = jqueryAjaxDriver

    constructor(
        readonly _ctor: ModelConstructor<T>,
    ) {

    }

    _makeURL(id?: id): string {
        if (id) {
            const dummy = new this._ctor({id: id})
            return dummy._objectURL()
        } else {
            const dummy = new this._ctor({})
            return dummy._collectionURL()
        }
    }

    async page(query: GetQuery<T>, page: PageQuery<T>, ajax_driver: AjaxDriver = this._ajax_driver): Promise<Collection<T>> {
        const data_to_send: any = {}
        Object.assign(data_to_send, query)
        if (page.limit) {
            data_to_send._limit = page.limit
        }
        if (page.page) {
            data_to_send._page = page.page
        }
        const json = await ajax_driver(data_to_send, this._makeURL(), 'GET')
        return new Collection(json, this._ctor)
    }

    async list(query: GetQuery<T>, ajax_driver: AjaxDriver = this._ajax_driver): Promise<T[]> {
        return (await this.page(query, {}, ajax_driver)).objects
    }

    async get(query: GetQuery<T>, ajax_driver: AjaxDriver = this._ajax_driver): Promise<T> {
        const collection = await this.page(query, {limit: 2, page: 1}, ajax_driver)
        if (collection.total > 1) {
            throw Error('received more than one element')
        } else if (collection.total == 0) {
            throw Error('no matching result')
        }
        return collection.objects[0]
    }
    // async update(query: UpdateQuery<T>): Promise<T> {
    //     const id = query.id
    //     delete query.id
    //     const _dummy = new this.ctor({ id: id })
    //     const json = await _dummy._ajax_driver(query, _dummy._objectURL(), 'PATCH')
    //     return new this.ctor(json)
    // }
    async create(query: CreateQuery<T>, ajax_driver: AjaxDriver = this._ajax_driver): Promise<T> {
        const json = await ajax_driver(query, this._makeURL(), 'POST')
        const obj = new this._ctor(json)
        obj._bind()
        return obj
    }
    // async delete(query: DeleteQuery): Promise<void> {
    //     const id = query.id
    //     delete query.id
    //     const _dummy = new this.ctor({ id: id })
    //     return _dummy._ajax_driver(query, _dummy._objectURL(), 'DELETE')
    // }
}
