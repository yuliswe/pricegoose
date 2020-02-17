
export type int = number
export type id = number

export const URLs = {
    LOGIN: "/api/v1/login",
    LOGOUT: "/api/v1/logout",
}


export type HttpMethod = 'DELETE' | 'POST' | 'GET' | 'PUT' | 'PATCH'
export type AjaxDriver = (data: Object, url: string, method: HttpMethod) => Promise<any>
