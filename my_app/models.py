import datetime
from django.db import models
from django.utils import timezone

class Bank(models.Model):
    bank_name = models.CharField(max_length=200)
    bank_url  = models.CharField(max_length=250)

    def __str__(self):
        return self.bank_name


class Offer(models.Model):
    bank                = models.ForeignKey(Bank, on_delete=models.CASCADE)
    offer_title         = models.CharField(max_length=200, blank = True)
    switch_bonus        = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    referral            = models.BooleanField(default=False)
    min_mthly_pay_in    = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    req_dd              = models.IntegerField(default=0)
    extra_perks         = models.CharField(max_length=500)
    fees                = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    fees_comment        = models.CharField(max_length=250, blank = True)
    monthly_bonus       = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    monthly_bonus_cmt   = models.CharField(max_length=250, blank = True)
    instructions        = models.TextField(blank = True) 
    monthly_interest    = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    terms               = models.TextField(blank = True) 
    offer_url           = models.CharField(max_length=250)
    start_date          = models.DateTimeField("Offer start date")
    end_date            = models.DateTimeField("Offer end date")

    def __str__(self):
       return self.bank.bank_name

