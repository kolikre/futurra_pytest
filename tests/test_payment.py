from pom.page_object import LandingPage


class TestPayment:
    URL = 'https://ironvpn.me/?source=test'
    EMAIL = 'qa@test.com'
    VALID_CARD_DATA = {
        'number': '4532456618142692',
        'date': '032029',
        'cvv': '967'
    }

    def test_positive_payment(self, setup):
        """ Positive payment test """
        driver = setup
        driver.get(self.URL)
        lp = LandingPage(driver)

        lp.openEmailModal()
        lp.setEmail(self.EMAIL)
        lp.clickPrivacyPolicyCheckbox()
        lp.clickApproveEmailButton()
        lp.openPaymentModalWindow()
        lp.typeCreditCardDataAndPay(self.VALID_CARD_DATA)
        title = driver.title

        assert title == 'SUCCESSFUL'
