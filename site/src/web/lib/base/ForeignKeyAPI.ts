import * as m from './Model'
import {AjaxDriver} from './base'
import {jqueryAjaxDriver} from './jqueryAjaxDriver'
import {RelationMixin} from './RelationMixin'

export class ForeignKeyAPI<R extends m.Model, T extends m.Model> {
    readonly _relation_mixin: RelationMixin<R, T>
    readonly _ajax_driver: AjaxDriver = jqueryAjaxDriver

    constructor(
        readonly _related_object: R,
        readonly _ctor: m.ModelConstructor<T>,
    ) {
        this._relation_mixin = new RelationMixin(_related_object, this)
    }

    async get(ajax_driver: AjaxDriver = this._ajax_driver): Promise<T> {
        const object = await ajax_driver({}, this._relation_mixin._makeURL(), 'GET')
        const model_object = new this._ctor(object)
        model_object._bind()
        return model_object
    }
}
