from django.contrib import admin
from .models import Bank, Offer

admin.site.register(Bank)
class OfferAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['bank','offer_title']}),
        ('Offer details',    {'fields': ['switch_bonus','referral','min_mthly_pay_in','req_dd','monthly_bonus','monthly_bonus_cmt','monthly_interest']}),
        ('Fees',             {'fields': ['fees','fees_comment']}),
        ('Extra Perks',      {'fields': ['extra_perks']}),
        ('URL to offer',     {'fields': ['offer_url']}),
        ('Instructions',     {'fields': ['instructions']}),
        ('Terms',            {'fields': ['terms']}),
        ('Date information', {'fields': ['start_date','end_date']}),
    ]

admin.site.register(Offer, OfferAdmin)

