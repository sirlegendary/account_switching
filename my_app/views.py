from django.shortcuts import render
from django.views import generic

from .models import Bank, Offer

def home(request):
    return render(request, 'base.html')

def new_search(request):

    monthly_income = request.POST.get('monthly_income')
    direct_debits = request.POST.get('direct_debits')
    money_saved = request.POST.get('money_saved')
    
    
    if monthly_income != "" and direct_debits != "" and money_saved != "":

        # offer_list = Offer.objects.filter(min_mthly_pay_in__lte=monthly_income,req_dd__lte=direct_debits) 

        offer_list = Offer.objects.all()

        print(list(offer_list))

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
