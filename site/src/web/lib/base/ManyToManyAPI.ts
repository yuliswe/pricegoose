import * as $ from "jquery"
import * as Cookies from 'js-cookie'

import {id, AjaxDriver} from './base'
import {jqueryAjaxDriver} from './jqueryAjaxDriver'
import {API} from "./API"
import {RelationMixin} from "./RelationMixin"
import {Model, ModelConstructor, Collection} from "./Model"
import {HttpMethod} from './base'

export class ManyToManyAPI<R extends Model, T extends Model> extends API<T>
{
    readonly _relation_mixin: RelationMixin<R, T>
    readonly _ajax_driver: AjaxDriver = jqueryAjaxDriver

    public constructor(
        _related_object: R,
        _ctor: ModelConstructor<T>,
    ) {
        super(_ctor)
        this._relation_mixin = new RelationMixin(_related_object, this)
    }

    _makeURL(id?: id) {
        return this._relation_mixin._makeURL()
    }

    async set(target: id | id[] | T | T[], ajax_driver: AjaxDriver = this._ajax_driver): Promise<T> {
        if (target instanceof Model) {
            return this._send('PATCH', target, ajax_driver)
        } else if (target instanceof Array) {
            return this._send('PUT', target, ajax_driver)
        } else {
            throw Error(`cannot set ${target} on ${this}`)
        }
    }

    async add(target: id | id[] | T | T[], ajax_driver: AjaxDriver = this._ajax_driver): Promise<T> {
        return this._send('POST', target, ajax_driver)
    }

    async remove(target: id | id[] | T | T[], ajax_driver: AjaxDriver = this._ajax_driver): Promise<T> {
        return this._send('DELETE', target, ajax_driver)
    }

    async _send(method: HttpMethod, data: id | id[] | T | T[], ajax_driver: AjaxDriver = this._ajax_driver): Promise<T> {
        if (data instanceof Array) {
            const target_ids = []
            for (const t of data) {
                if (typeof t === 'number') {
                    target_ids.push(t)
                } else if (typeof t === 'string') {
                    target_ids.push(Number.parseInt(t))
                } else if (data instanceof Model) {
                    target_ids.push(t.id)
                } else {
                    throw Error(`Cannot call _send with data ${data} containing item ${t} of type ${typeof t}`)
                }
            }
            return ajax_driver(target_ids, this._makeURL(), method)
        } else if (typeof data === "number") {
            return ajax_driver(data, this._makeURL(), method)
        } else if (typeof data === "string") {
            return ajax_driver(Number.parseInt(data), this._makeURL(), method)
        } else if (data instanceof Model) {
            return ajax_driver(data.id, this._makeURL(), method)
        } else {
            throw Error(`Cannot call _send with data ${data} of type ${typeof data}`)
        }
    }
}
