
# Import modules
import data
import pages
# import helpers
from helpers import is_url_reachable, retrieve_phone_code
import time
from selenium import webdriver
from pages import UrbanRoutesPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        cls.driver.implicitly_wait(5)

        if is_url_reachable(data.URBAN_ROUTES_URL):
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_set_route(self):
        # Test that sets the route
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Check for the value in the "From" input field
        from_input = self.driver.find_element(*UrbanRoutesPage.FROM_LOCATOR).get_attribute("value")
        assert from_input == data.ADDRESS_FROM, f"Expected FROM '{data.ADDRESS_FROM}', but got '{from_input}'"

        # Check for the value in the "To" input field
        to_input = self.driver.find_element(*UrbanRoutesPage.TO_LOCATOR).get_attribute("value")
        assert to_input == data.ADDRESS_TO, f"Expected TO '{data.ADDRESS_TO}', but got '{to_input}'"

    def test_select_plan(self):
        # Test that selects a plan
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.CALL_TAXI_ICON_LOCATOR))
        urban_routes_page.click_call_taxi_icon()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.SUPPORTIVE_ICON_LOCATOR))
        urban_routes_page.click_supportive_icon()

        # Assert that the supportive plan is now active
        plan_element = self.driver.find_element(*UrbanRoutesPage.SUPPORTIVE_ICON_LOCATOR)
        assert 'active' in plan_element.get_attribute('class'), "Supportive plan should be active but isn't"

    def test_fill_phone_number(self):
        # Test that add phone number
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.CALL_TAXI_ICON_LOCATOR))
        urban_routes_page.click_call_taxi_icon()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.SUPPORTIVE_ICON_LOCATOR))
        urban_routes_page.click_supportive_icon()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        sms_code = retrieve_phone_code(self.driver)
        urban_routes_page.sms_phone_code(sms_code)

        # Check the value in the "phone number" input field
        phone_input = self.driver.find_element(*UrbanRoutesPage.ENTER_PHONE_NUMBER_LOCATOR).get_attribute("value")
        assert phone_input == data.PHONE_NUMBER, f"Expected phone number is '{data.PHONE_NUMBER}', but got '{phone_input}'"

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.CALL_TAXI_ICON_LOCATOR))
        urban_routes_page.click_call_taxi_icon()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.SUPPORTIVE_ICON_LOCATOR))
        urban_routes_page.click_supportive_icon()
        urban_routes_page.adding_new_card(data.CARD_NUMBER, data.CARD_CODE)

        # Check the value in the "card number" input field
        card_input = self.driver.find_element(*UrbanRoutesPage.ADD_CARD_NUMBER_LOCATOR).get_attribute("value")
        assert card_input == data.CARD_NUMBER, f"Expected card number is '{data.CARD_NUMBER}', but got '{card_input}'"

        # Check the value in the "card code" input field
        code_input = self.driver.find_element(*UrbanRoutesPage.ADD_CARD_CODE_LOCATOR).get_attribute("value")
        assert code_input == data.CARD_CODE, f"Expected code is '{data.CARD_CODE}', but got '{code_input}'"

    def test_comment_for_driver(self):
        # Test that adds comment for a driver
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.CALL_TAXI_ICON_LOCATOR))
        urban_routes_page.click_call_taxi_icon()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.SUPPORTIVE_ICON_LOCATOR))
        urban_routes_page.click_supportive_icon()
        urban_routes_page.message_driver(data.MESSAGE_FOR_DRIVER)

        #check that messages matches
        comment_input = self.driver.find_element(*UrbanRoutesPage.MESSAGE_TO_DRIVER_LOCATOR).get_attribute("value")
        assert comment_input == data.MESSAGE_FOR_DRIVER, f"Expected FROM '{data.MESSAGE_FOR_DRIVER}', but got '{comment_input}'"

    def test_order_blanket_and_handkerchiefs(self):
        # Test that orders blanket and handkerchiefs
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.CALL_TAXI_ICON_LOCATOR))
        urban_routes_page.click_call_taxi_icon()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.SUPPORTIVE_ICON_LOCATOR))
        urban_routes_page.click_supportive_icon()
        urban_routes_page.blanket_handkerchiefs()
        time.sleep(0.5)

        # Locate the element that changes background color
        bg_color = self.driver.find_element(*UrbanRoutesPage.BLANKET_HANDKERCHIEFS_LOCATOR).value_of_css_property('background-color')

        # Normalize to RGB format by removing alpha if it's 1
        normalized_color = bg_color.replace('rgba', 'rgb').replace(', 1)', ')')

        # Compare with expected RGB value
        expected_rgb = 'rgb(0, 126, 255)' # equivalent to hex color #007eff
        assert normalized_color == expected_rgb, f"Expected '{expected_rgb}', but got '{bg_color}'"

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.CALL_TAXI_ICON_LOCATOR))
        urban_routes_page.click_call_taxi_icon()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.SUPPORTIVE_ICON_LOCATOR))
        urban_routes_page.click_supportive_icon()
        urban_routes_page.add_ice_cream()

        #check that 2 ice creams were ordered
        ice_cream_quantity = self.driver.find_element(*UrbanRoutesPage.ICE_CREAM_QUANTITY).text
        expected_quantity = '2'
        assert ice_cream_quantity == expected_quantity, f"Expected ice cream quantity to be '2', but got '{ice_cream_quantity}'"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.CALL_TAXI_ICON_LOCATOR))
        urban_routes_page.click_call_taxi_icon()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(pages.UrbanRoutesPage.SUPPORTIVE_ICON_LOCATOR))
        urban_routes_page.click_supportive_icon()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        sms_code = retrieve_phone_code(self.driver)
        urban_routes_page.sms_phone_code(sms_code)
        urban_routes_page.adding_new_card(data.CARD_NUMBER, data.CARD_CODE)
        urban_routes_page.message_driver(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.order_taxi()

        modal = self.driver.find_element(*UrbanRoutesPage.CAR_SEARCH_LOCATOR)
        assert modal.is_displayed(), "Expected car search modal to appear after activating Order Taxi button"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
