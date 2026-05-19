from django.test import TestCase


class CoreAppTestCase(TestCase):

    def test_home_route_of_app(self):
        # Issue a GET request.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the content of the response contains messgae.
        self.assertEqual(response.content, b'{"message": "Welcome to FAER API"}')
