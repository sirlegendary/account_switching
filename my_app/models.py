import datetime
from django.db import models
from django.utils import timezone

class Bank(models.Model):
    bank_name = models.CharField(max_length=200)
    bank_url  = models.CharField(max_length=200)

    def __str__(self):
        return self.bank_name


class Offer(models.Model):
    bank                = models.ForeignKey(Bank, on_delete=models.CASCADE)
    switch_bonus        = models.IntegerField(default=0)
    referral            = models.BooleanField(default=False)
    min_mthly_pay_in    = models.IntegerField(default=0)
    req_dd              = models.IntegerField(default=0)
    extra_perks         = models.CharField(max_length=200)
    offer_url           = models.CharField(max_length=250)
    start_date          = models.DateTimeField("Offer start date")
    end_date            = models.DateTimeField("Offer end date")

    def __str__(self):
       return self.bank.bank_name