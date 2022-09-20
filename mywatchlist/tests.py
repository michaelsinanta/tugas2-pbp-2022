from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class myWatchListTest(TestCase):
    def test_html_exists(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_html"))
        self.assertEquals(response.status_code, 200)
    
    def test_xml_exists(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_xml"))
        self.assertEquals(response.status_code, 200)
    
    def test_json_exists(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_json"))
        self.assertEquals(response.status_code, 200)