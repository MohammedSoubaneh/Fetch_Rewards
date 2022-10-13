from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import json


class TransactionTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.url = reverse('send_transaction')
        self.list_url = reverse('list_transaction')
        self.spend_points_url = reverse('spend_points')

        self.data = {
            "user": 1,
            "payer": "Soub",
            "points": 300
        }
        self.data_two = {
            "user": 1,
            "payer": "Moe",
            "points": 6000        
        }
        self.spend_points_data = {
            "points": 302
        }


    def test_get_transactions(self):
        url = reverse('list_transaction')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_post_transaction(self):
        response = self.client.post(self.url, self.data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_spend_points(self):
        spend_points_data = {
            "points": 300
        }
        self.client.post(self.url, self.data, format="json")
        self.client.post(self.spend_points_url, spend_points_data, format="json")
        response = self.client.get(self.list_url, format="json")
        self.assertEqual(json.loads(response.content)[0]["points"], 0)


    def test_spend_multiple_points(self):
        spend_points_two = {
            "points": 4000
        }
        self.client.post(self.url, self.data, format="json")
        self.client.post(self.url, self.data_two, format="json")
        self.client.post(self.spend_points_url, spend_points_two, format="json")
        response = self.client.get(self.list_url, format="json")
        self.assertEqual(json.loads(response.content)[0]["points"], 0)
        self.assertEqual(json.loads(response.content)[1]["points"], 2300)