from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TransactionTest(TestCase):

    def test_get_transactions(self):
        url = reverse('list_transaction')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_post_transaction(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        url = reverse('send_transaction')
        data = {
            "payer": 1,
            "points": 350
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)