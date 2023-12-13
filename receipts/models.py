from django.db import models
from django.contrib.auth.models import User


class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.CharField(max_length=50)
    items_list = models.TextField(null=True, blank=True)
    purchase_date = models.DateField(auto_now_add=False)
    amount = models.FloatField()

