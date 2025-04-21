
# Import modules
import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Checks if server is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_set_route(self):
        # Placeholder for a test that sets the route
        # Add in S8
        print('function created for set route')
        pass

    def test_select_plan(self):
        # Placeholder for a test that selects a plan
        # Add in S8
        print('function created for select plan')
        pass

    def test_fill_phone_number(self):
        # Placeholder for a test that fills a phone number
        # Add in S8
        print('function created for fill phone number')
        pass

    def test_fill_card(self):
        # Placeholder for a test that fills a card
        # Add in S8
        print('function created for fill card')
        pass

    def test_comment_for_driver(self):
        # Placeholder for a test that add comment for a driver
        # Add in S8
        print('function created for comment for driver')
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Placeholder for a test that orders blanket and handkerchiefs
        # Add in S8
        print('function created for order blanket and handkerchiefs')
        pass

    def test_order_2_ice_creams(self):
        for x in range(2):
            # Placeholder for a test that orders ice creams
            # Add in S8
            print('function created for order 2 ice creams')
            pass

    def test_car_search_model_appears(self):
        # Placeholder for a test that searches for car models
        # Add in S8
        print('function created for car search model appears')
        pass


