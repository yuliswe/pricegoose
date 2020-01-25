describe('before login, when adding product to basket in category view,', () => {

    it('user should be asked to log in', () => {
        browser.url('/catalogue/c/181')
        $('.-test-add-to-cart-button').click()
        $('.-test-login-inputs').waitForDisplayed(1000)
    })

})

describe('after login', () => {

    beforeEach(() => {
        browser.url('/tests/login')
    })

    describe('add a product to basket from category 181', () => {

        beforeEach(() => {
            browser.url('/catalogue/c/181')
            $('.-test-add-to-cart-button').click()
        })

        it('route should be /basket/added', () => {
            const loc = browser.getUrl()
            expect(loc).to.contain('/basket/added')
        })

        it('.-test-added-success-hint should display', () => {
            assert($('.-test-add-success-hint').isDisplayed())
        })

        it('product should be added to basket', () => {
            assert($('.-test-product-list-item').isDisplayed())
        })

        it('product count should be 1', () => {
            $('.-test-quantity-control').setValue('1')
            $('.-test-quantity-control').keys('Return')
            const count = $('.-test-quantity-control').getValue()
            expect(count).to.equal('1')
        })

        describe('remove product', () => {

            beforeEach(() => {
                $('.-test-delete-button').click()
            })

            it('route should be /basket/removed', () => {
                const loc = browser.getUrl()
                expect(loc).to.contain('/basket/removed')
            })

            it('.-test-remove-success-hint should display', () => {
                assert($('.-test-remove-success-hint').isDisplayed())
            })
        })

        describe('decrease product count', () => {

            beforeEach(() => {
                $('.-test-quantity-control-minus').click()
            })

            it('product count should still be 1 (should not be less than 1)', () => {
                const count = $('.-test-quantity-control').getValue()
                expect(count).to.equal('1')
            })
        })

        describe('increase product count', () => {

            beforeEach(() => {
                $('.-test-quantity-control-plus').click()
            })

            it('product count should become 2', () => {
                const count = $('.-test-quantity-control').getValue()
                expect(count).to.equal('2')
            })

        })

        describe('decrease product count', () => {

            beforeEach(() => {
                $('.-test-quantity-control-minus').click()
            })

            it('product count should return to 1', () => {
                const count = $('.-test-quantity-control').getValue()
                expect(count).to.equal('1')
            })
        })

        describe('place order', () => {

            beforeEach(() => {
                $('.-test-go-to-payment-button').click()
            })

            it('route should be /basket/delivery', () => {
                const loc = browser.getUrl()
                expect(loc).to.contain('/basket/delivery')
            })
        })

    })
})
