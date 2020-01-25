const assert = require('assert')

describe('visiting these urls to check for console errors:', () => {
    it('/', () => { browser.url('/') })
    it('/admin', () => { browser.url('/admin') })
})