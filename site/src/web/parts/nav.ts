import './nav.scss'
import './login'
import './user-profile'
import * as lib from 'lib'
import * as $ from 'jquery'

export function init() {
    $('[data-js-open-user-profile]').on('click', () => {
        console.log('show login', $('*[data-js-user-profile-container]'))
        $('[data-js-user-profile-container]').toggleClass('show');
    })
    $('[data-js-open-login]').on('click', () => {
        console.log('show login', $('*[data-js-login-container]'))
        $('[data-js-login-container]').toggleClass('show');
    })
    $('[data-js-signout]').click(async () => {
        await lib.Logout.logout()
        location.reload()
    })
}
