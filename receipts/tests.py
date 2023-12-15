import unittest
from django.contrib.auth.models import User
from .models import Receipt

class ReceiptModelTest(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.receipt = Receipt.objects.create(
            user=self.user,
            store='Test Store',
            items_list='Item 1, Item 2',
            purchase_date='2023-12-01',
            amount=100.00
        )

    def test_receipt_user(self):
        self.assertEqual(self.receipt.user, self.user)

    def test_receipt_store(self):
        self.assertEqual(self.receipt.store, 'Test Store')

    def test_receipt_items_list(self):
        self.assertEqual(self.receipt.items_list, 'Item 1, Item 2')

    def test_receipt_purchase_date(self):
        self.assertEqual(str(self.receipt.purchase_date), '2023-12-01')

    def test_receipt_amount(self):
        self.assertEqual(self.receipt.amount, 100.00)

    def tearDown(self):
        self.receipt.delete()
        self.user.delete()