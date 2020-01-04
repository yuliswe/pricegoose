import * as $ from "jquery"
import Cookies from 'js-cookie'

export type int = number
export type id = number

export class DEEP { id: 1 }
export class SHALLOW { id: 2 }

export const URLs = {
    PRODUCT: "/api/v1/products",
    CATEGORY: "/api/v1/categories",
    CATEGORY_PRODUCT: "/api/v1/product_categories",
    PRODUCT_IMAGE: "/api/v1/product_images",
    BASKET_PRODUCT: "/api/v1/basket_products",
    UPLOAD: "/api/v1/upload",
    LOGIN_VIA_GOOGLE: "/api/login",
    LOGOUT: "/api/logout",
    SESSION: "/api/v1/session",
    SESSION_BASKET: "/api/v1/session/basket",
    SESSION_BASKET_PRODUCT: "/api/v1/session/basket_products",
}

export interface Collection<T> {
    page: int
    limit: int
    count: int
    previous: string
    next: string
    objects: T[]
}

export interface ListQuery {
    page?: int
    limit?: int
}

export interface GetQuery {
    id: id
}

export interface DeleteQuery {
    id: id
}

export type CreateQuery<T> = Partial<Omit<T, 'id'>>
export type UpdateQuery<T> = Partial<Omit<T, 'id'>> & { id: id }

export class ObjectAPI<T_SHALLOW, T_DEEP>
{
    public readonly URL: string = '';
    public async list(query: ListQuery): Promise<Collection<T_SHALLOW>> {
        return await $.ajax({
            data: query,
            dataType: 'json',
            url: this.URL,
            method: 'GET'
        })
    }

    public async get(query: GetQuery): Promise<T_DEEP> {
        return await $.ajax({
            data: query,
            dataType: 'json',
            url: `${this.URL}/${query.id}`,
            method: 'GET'
        })
    }

    public async update(query: UpdateQuery<T_SHALLOW>): Promise<T_DEEP> {
        return await $.ajax({
            data: JSON.stringify(query),
            contentType: "application/json; charset=UTF-8",
            dataType: 'json',
            url: `${this.URL}/${query.id}`,
            method: 'PATCH',
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
        })
    }

    public async create(query: CreateQuery<T_SHALLOW>): Promise<T_DEEP> {
        return await $.ajax({
            data: JSON.stringify(query),
            contentType: "application/json; charset=UTF-8",
            dataType: 'json',
            url: this.URL,
            method: 'POST',
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
        })
    }

    public async delete(query: DeleteQuery): Promise<void> {
        return await $.ajax({
            data: JSON.stringify(query),
            contentType: "application/json; charset=UTF-8",
            dataType: 'json',
            url: `${this.URL}/${query.id}`,
            method: 'DELETE',
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
        })
    }
}
