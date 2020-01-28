describe('Test google login (sequential)', () => {
    browser.url('/')

    it('click login at nav bar', () => {
        $('[data-js-open-login]').waitForDisplayed()
        $('[data-js-open-login]').click()
    })
    it('[data-js-login-container] should display', () => {
        $('[data-js-login-container]').waitForDisplayed()
    })
    it('click google login button', () => {
        $('[data-js-google-signin-button]').click()
    })
    it('oauth window should display', () => {
        browser.waitUntil(() => browser.getWindowHandles().length > 1)
        browser.switchToWindow(browser.getWindowHandles()[1])
    })
    it('type in email address', () => {
        $('input[type=email]').waitForDisplayed()
        $('input[type=email]').addValue('pricegoose.ui.tester.1@gmail.com')
    })
    it('click "Next" button', () => {
        $('#identifierNext,input[type=submit]').click()
    })
    it('type in password', () => {
        $('input[type=password]').waitForDisplayed()
        $('input[type=password]').addValue('#123asdf')
    })
    it('click "Next" button', () => {
        $('#passwordNext,input[type=submit]').click()
    })
    it('oauth window should close', function() {
        if (process.env.CI_RUN) {
            this.skip()
        }
        browser.waitUntil(() => browser.getWindowHandles().length == 1)
        browser.switchToWindow(browser.getWindowHandles()[0])
    })
    it('observe login button disappears from nav bar', () => {
        if (process.env.CI_RUN) {
            this.skip()
        }
        $('[data-js-open-user-profile]').waitForDisplayed()
    })
})
