from django.contrib import admin
from .models import Bank, Offer

admin.site.register(Bank)
class OfferAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['bank']}),
        ('Offer details',    {'fields': ['switch_bonus','referral','min_mthly_pay_in','req_dd','extra_perks']}),
        ('URL to offer',     {'fields': ['offer_url']}),
        ('Date information', {'fields': ['start_date','end_date']}),
    ]

admin.site.register(Offer, OfferAdmin)
