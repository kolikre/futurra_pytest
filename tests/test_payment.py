import configs.config as config
from pom.page_object import LandingPage


class TestPayment:

    def test_positive_payment(self, setup):
        """ Positive payment test """
        driver = setup
        driver.get(config.URL)
        lp = LandingPage(driver)
        lp.openEmailModal()
        lp.setEmail(config.EMAIL)
        lp.clickPrivacyPolicyCheckbox()
        lp.clickApproveEmailButton()
        lp.openPaymentModalWindow()
        lp.typeCreditCardDataAndPay(config.VALID_CARD_DATA)
        title = driver.title
        assert title == 'SUCCESSFUL'
