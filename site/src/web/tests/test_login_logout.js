describe('before login', () => {

    describe('login using mobile 0000000000, code 0000', () => {
        it('[data-test-mobile-number] should have text 0000000000', () => {
            browser.url('/')
            const login_link = $('[data-test-login-link]').click()
            const login_modal = $('[data-test-login-modal]')
            login_modal.$('input[name="mobile_number"]').addValue('0000000000')
            login_modal.$('input[name="code_text"]').addValue('0000')
            login_modal.$('[data-test-login-button]').click()
            const mobile_number = $('[data-test-mobile-number]')
            expect(mobile_number.getText()).to.equal('0000000000')
        })
    })

    describe('logout', () => {
        it('[data-test-mobile-number] should be hidden', () => {
            browser.url('/tests/login')
            browser.url('/')
            $('[data-test-mobile-number]').click()
            $('.-test-logout-link').click()
            browser.url('/')
            const mobile_number = $('[data-test-mobile-number]')
            assert(!mobile_number.isExisting())
        })
    })
})
