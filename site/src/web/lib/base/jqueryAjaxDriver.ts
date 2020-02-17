import * as $ from "jquery"
import * as Cookies from 'js-cookie'
import {HttpMethod} from './base'

export function jqueryAjaxDriver(data: Record<string, string | number | boolean>, url: string, method: HttpMethod) {
    const promise = new Promise((resolve, reject) => {
        const result = $.ajax({
            data: method == 'GET' ? data : JSON.stringify(data),
            contentType: "application/json; charset=UTF-8",
            dataType: 'json',
            url: url,
            method: method,
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            success: resolve,
            error: reject,
        })
    })
    return promise
}
