from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_ICON_LOCATOR = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    SUPPORTIVE_ICON_LOCATOR = (By.XPATH, '//div[@class="tcard-icon"]//img[@src="/static/media/kids.27f92282.svg"]/ancestor::div[contains(@class, "tcard")]')
    PHONE_NUMBER_LOCATOR = (By.XPATH, '//div[@class="np-text"]')
    ENTER_PHONE_NUMBER_LOCATOR = (By.ID, 'phone')
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Next")]')
    ENTER_CODE_LOCATOR = (By.ID, 'code')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Confirm")]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-text"]')
    ADD_NEW_CARD_LOCATOR = (By.XPATH, '//div[contains(text(), "Add card")]')
    ADD_CARD_NUMBER_LOCATOR = (By.ID, 'number')
    ADD_CARD_CODE_LOCATOR = (By.XPATH, '//input[@placeholder="12"]')
    CLICK_FORM_LOCATOR = (By.XPATH, '//div[@class="card-wrapper"]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Link")]')
    CLOSE_PAYMENT_OPTION_LOCATOR = (By.XPATH, '(//div[@class="section active"]//button[@class="close-button section-close"])[2]')
    MESSAGE_TO_DRIVER_LOCATOR = (By.ID, 'comment')
    BLANKET_HANDKERCHIEFS_LOCATOR = (By.XPATH, '(//span[@class="slider round"])[1]')
    ICE_CREAM_LOCATOR = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    ICE_CREAM_QUANTITY = (By.XPATH, '(//div[@class="counter-value"])[1]')
    ORDER_BUTTON = (By.XPATH, '//button[@class="smart-button"]')
    CAR_SEARCH_LOCATOR = (By.XPATH, '(//div[@class="overlay"])[3]')

    def __init__(self, driver):
        self.driver = driver

    def enter_locations(self, from_text, to_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_call_taxi_icon(self):
        self.driver.find_element(*self.CALL_TAXI_ICON_LOCATOR).click()

    def click_supportive_icon(self):
        plan = self.driver.find_element(*self.SUPPORTIVE_ICON_LOCATOR)
        if 'active' not in plan.get_attribute('class'):
            plan.click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).click()
        self.driver.find_element(*self.ENTER_PHONE_NUMBER_LOCATOR).send_keys(phone_number)
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()

    def sms_phone_code(self, sms_code):
        self.driver.find_element(*self.ENTER_CODE_LOCATOR).send_keys(sms_code)
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def adding_new_card(self, card_number, cc_code):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()
        self.driver.find_element(*self.ADD_NEW_CARD_LOCATOR).click()
        self.driver.find_element(*self.ADD_CARD_NUMBER_LOCATOR).send_keys(card_number)
        self.driver.find_element(*self.ADD_CARD_CODE_LOCATOR).send_keys(cc_code)
        self.driver.find_element(*self.CLICK_FORM_LOCATOR).click()
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.CLOSE_PAYMENT_OPTION_LOCATOR).click()

    def message_driver(self, message):
        self.driver.find_element(*self.MESSAGE_TO_DRIVER_LOCATOR).send_keys(message)

    def blanket_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_HANDKERCHIEFS_LOCATOR).click()

    def add_ice_cream(self):
        for x in range(2):
            self.driver.find_element(*self.ICE_CREAM_LOCATOR).click()

    def order_taxi(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()


