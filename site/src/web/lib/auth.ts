import {URLs} from './base'
import * as Cookies from 'js-cookie'
import * as $ from "jquery"

export class LoginAPI {
    public async viaGoogleToken() {
        const google_auth: any = await new Promise(function(resolve, reject) {
            window['gapi'].load('auth2', () => {
                return resolve(window['gapi'].auth2.init())
            })
        })
        const google_user = google_auth.currentUser.get()
        const id_token = google_user.getAuthResponse().id_token
        try {
            await $.ajax(URLs.LOGIN, {
                method: 'POST',
                dataType: 'json',
                headers: {
                    'X-CSRFToken': Cookies.get('csrftoken'),
                },
                data: {
                    'token': id_token,
                },
            })
        } catch (e) {
            console.error('bad login')
            throw e
        }
        finally {
            google_auth.signOut()
        }
    }
}

export class LogoutAPI {
    public async logout() {
        return $.ajax(URLs.LOGOUT, {
            method: 'POST',
            dataType: 'json',
            headers: {
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
        })
    }
}
