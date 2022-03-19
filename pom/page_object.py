import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class LandingPage:
    """ Landing page object model """
    open_email_modal_window_email_button = '//button[@data-hystmodal="#modalForms" and @class="btn"]'
    email_input_field = '//input[@id="email"]'
    submit_email_button = '//button[@id="validate"]'
    privacy_policy_checkbox = '//i[@class="checkplace"]'
    open_payment_iframe_button = '//section[@id="trial"]//span[contains(text(), "Get IronVPN Now")]//parent::a'
    iframe_card_number_input_field = '//form[@name="paymentForm"]//input[@name="cardNumber"]'
    iframe_card_expiration_input_field = '//form[@name="paymentForm"]//input[@name="cardExpiryDate"]'
    iframe_card_cvv_input_field = '//form[@name="paymentForm"]//input[@name="cardCvv"]'
    iframe_payment_form = '//iframe[@id="solid-payment-form-iframe"]'
    iframe_submit_payment_button = '//form[@name="paymentForm"]//button'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.1)

    def openEmailModal(self):
        """ Click button to open modal window with email input field """
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.open_email_modal_window_email_button)))
        self.driver.find_element(By.XPATH, self.open_email_modal_window_email_button).click()

    def setEmail(self, email):
        """ Insert email into email field """
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.email_input_field)))
        self.driver.find_element(By.XPATH, self.email_input_field).send_keys(email)

    def clickPrivacyPolicyCheckbox(self):
        """ Clic to privacy policy checkbox """
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.privacy_policy_checkbox)))
        self.driver.find_element(By.XPATH, self.privacy_policy_checkbox).click()

    def clickApproveEmailButton(self):
        """ Click approve button in email modal window """
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.submit_email_button)))
        self.driver.find_element(By.XPATH, self.submit_email_button).click()

    def openPaymentModalWindow(self):
        """ Click button to open iframe payment form """
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.open_payment_iframe_button)))
        self.driver.find_element(By.XPATH, self.open_payment_iframe_button).click()

    def typeCreditCardDataAndPay(self, data):
        """ Insert and approve credit card data into iframe payment form """
        # Switch to iframe
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.iframe_payment_form)))
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.iframe_payment_form))
        time.sleep(1)
        # Insert card number
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.iframe_card_number_input_field)))
        self.driver.find_element(By.XPATH, self.iframe_card_number_input_field).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.iframe_card_number_input_field).send_keys(data['number'])
        time.sleep(0.5)
        # Insert expiration card date
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.iframe_card_expiration_input_field)))
        self.driver.find_element(By.XPATH, self.iframe_card_expiration_input_field).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.iframe_card_expiration_input_field).send_keys(data['date'])
        time.sleep(0.5)
        # Insert cvv code
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.iframe_card_cvv_input_field)))
        self.driver.find_element(By.XPATH, self.iframe_card_cvv_input_field).click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.iframe_card_cvv_input_field).send_keys(data['cvv'])
        time.sleep(0.5)
        # Click "Pay" button
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.iframe_submit_payment_button)))
        self.driver.find_element(By.XPATH, self.iframe_submit_payment_button).click()
        # Switch from iframe to main content and wait until iframe disappear
        self.driver.switch_to.default_content()
        self.wait.until(ec.invisibility_of_element_located((By.XPATH, self.iframe_payment_form)))
