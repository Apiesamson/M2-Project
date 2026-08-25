from django.test import TestCase, Client

# Create your tests here.

class HomePageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_status_code(self):
        """Vérifie que la page d'accueil répond avec succès (code 200)"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
