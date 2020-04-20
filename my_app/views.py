import json
import re
from django.shortcuts import get_object_or_404, render
from django.views import generic


from my_app.models import Bank, Offer

def home(request):
    return render(request, 'base.html')

def new_search(request):

    monthly_income = request.POST.get('monthly_income')
    direct_debits = request.POST.get('direct_debits')
    money_saved = request.POST.get('money_saved')
    
    
    if monthly_income != "" and direct_debits != "" and money_saved != "":

        offer_filtered = Offer.objects.filter(min_mthly_pay_in__lte=monthly_income,req_dd__lte=direct_debits) 

        offer_list = []
        for a in Offer.objects.filter(min_mthly_pay_in__lte=monthly_income,req_dd__lte=direct_debits):
            abc = a.bank
            t = {
                'bank':abc,
                'switch_bonus':a.switch_bonus,
                'referral':a.referral,
                'min_mthly_pay_in':a.min_mthly_pay_in,
                'req_dd':a.req_dd,             
                'extra_perks':a.extra_perks,         
                'offer_url':a.offer_url,           
                'start_date':a.start_date,       
                'end_date':a.end_date,           
            }
            offer_list.append(t)
            print (f"URL: {a.offer_url} and Start Date: {a.start_date} Bank: {abc}")


        stuff_for_frontend = {
            'monthly_income': monthly_income,
            'direct_debits': direct_debits,
            'money_saved':money_saved,
            'offer_list': offer_list,
        }
        return render(request, 'my_app/new_search.html', stuff_for_frontend)
    else:
        stuff_for_frontend = {
            'error_message': "You have to fill out all fields.",
        }
        return render(request, 'my_app/new_search.html', stuff_for_frontend)
