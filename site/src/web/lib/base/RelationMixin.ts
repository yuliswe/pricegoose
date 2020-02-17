import * as m from './Model'
import {API} from './API'
import {Model} from "./Model"
import {id, AjaxDriver, HttpMethod} from './base'
import {ManyToManyAPI} from './ManyToManyAPI'
import {ForeignKeyAPI} from './ForeignKeyAPI'

export class RelationMixin<R extends m.Model, T extends m.Model> {
    constructor(
        readonly _related_object: R,
        readonly _key_field: ManyToManyAPI<R, T> | ForeignKeyAPI<R, T>,
    ) {
    }

    public _field_name_cached: string
    _makeURL(id?: id): string {
        if (this._field_name_cached === undefined) {
            for (const key in this._related_object) {
                if (key[0] === '_') {
                    continue // skip internal properties
                }
                const val = this._related_object[key] as unknown
                if (val === this._key_field) {
                    this._field_name_cached = key
                }
            }
        }
        if (id) {
            return `/api/v1/${this._related_object._name}/${this._related_object.id}/${this._field_name_cached}/${id}`
        } else {
            return `/api/v1/${this._related_object._name}/${this._related_object.id}/${this._field_name_cached}`
        }
    }
}
