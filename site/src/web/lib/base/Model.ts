
import {id} from './base'
import {AjaxDriver, int} from './base'
import {jqueryAjaxDriver} from './jqueryAjaxDriver'
import {ForeignKeyAPI} from './ForeignKeyAPI'

export interface ModelConstructor<T> {
    new(object: any): T
}

export class Collection<T extends Model> {
    page: int
    limit: int
    total: int
    previous: string
    next: string
    objects: T[]
    public constructor(data: Object, private ctor: ModelConstructor<T>) {
        Object.assign(this, data)
        for (const index in this.objects) {
            const object = this.objects[index]
            this.objects[index] = new this.ctor(object)
            this.objects[index]._bind()
        }
    }

    public async delete(): Promise<void> {
        for (const object of this.objects) {
            await object.delete()
        }
    }
}

export abstract class Model {
    readonly id: id
    readonly _updated_data = {}
    readonly abstract _name: string
    readonly _ajax_driver: AjaxDriver = jqueryAjaxDriver
    private _binded = false

    constructor(
        readonly _original_data,
    ) {
    }

    _bind() {
        this._binded = true
        function bindKey(key, get_or_set: ('get' | 'set')[]) {
            const prop = {}
            if (get_or_set.includes('get')) {
                prop['get'] = () => {
                    if (key in this._updated_data) {
                        return this._updated_data[key]
                    } else {
                        return this._original_data[key]
                    }
                }
            } else {
                const original_val = this[key]
                prop['get'] = () => {
                    return original_val
                }
            }
            if (get_or_set.includes('set')) {
                prop['set'] = (value: any) => {
                    if (this[key] === value) {
                        return value
                    }
                    if (this[key] instanceof ForeignKeyAPI) {
                        // product.brand = brand, product.brand = id,
                        // product.brand = null
                        if (typeof value === "number" || value === null || value instanceof Model) {
                            return this._updated_data[key] = value
                        }
                    } else if (typeof this[key] === undefined || typeof this[key] === typeof value) {
                        return this._updated_data[key] = value
                    } else if (typeof this[key] === 'number' && typeof value === 'string') {
                        return this._updated_data[key] = Number.parseFloat(value)
                    } else if (typeof this[key] === 'string' && typeof value === 'number') {
                        return this._updated_data[key] = value.toString()
                    }
                    throw Error(`Cannot set property ${key} of type ${typeof key} as value ${value} of type ${typeof value}`)
                }
            }
            Object.defineProperty(this, key, prop)
        }
        for (const key in this._original_data) {
            if (key in this) {
                bindKey.call(this, key, ['set'])
            } else {
                bindKey.call(this, key, ['get', 'set'])
            }
        }
    }

    _objectURL(): string {
        if (this.id === undefined) {
            throw 'access id undefined'
        }
        return `/api/v1/${this._name}/${this.id}`
    }
    _collectionURL(): string {
        return `/api/v1/${this._name}`
    }
    async delete(ajax_driver: AjaxDriver = this._ajax_driver): Promise<void> {
        return ajax_driver({}, this._objectURL(), 'DELETE')
    }
    async save(ajax_driver: AjaxDriver = this._ajax_driver): Promise<this> {
        if (Object.keys(this._updated_data).length === 0) {
            return this
        } else {
            const data_to_send = {}
            for (const key in this._updated_data) {
                data_to_send[key] = this._updated_data[key]
                if (data_to_send[key] instanceof Model) {
                    data_to_send[key] = data_to_send[key].id
                }
            }
            const json = await ajax_driver(data_to_send, this._objectURL(), 'PATCH')
            Object.assign(this._original_data, this._updated_data)
            const obj = new (this.constructor as ModelConstructor<this>)(json)
            obj._bind()
            return obj
        }
    }
}
