from django.test import Client, TestCase

class HikesTestCase(TestCase):
    def setUp(self):
        HikesTestCase.client = Client()

    def test_hikes_endpoint(self):
        """GET requests to the hikes endpoint give us a 200 status"""
        response = HikesTestCase.client.get('/gorapass/hikes')
        self.assertEqual(response.status_code, 200)