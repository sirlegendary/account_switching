import json
import datetime
from django.utils import timezone
from django.shortcuts import render


from my_app.models import Bank, Offer

def home(request):
    return render(request, 'base.html')

def new_search(request):

    monthly_income = request.POST.get('monthly_income')
    direct_debits = request.POST.get('direct_debits')
    money_saved = request.POST.get('money_saved')
    
    
    if monthly_income != "" and direct_debits != "" and money_saved != "" and monthly_income != None and direct_debits != None and money_saved != None:

        today = timezone.now()

        offer_filtered = Offer.objects.filter(min_mthly_pay_in__lte=monthly_income,req_dd__lte=direct_debits,end_date__gte=today).order_by('end_date')

        print(offer_filtered)

        offer_list = []
        for a in Offer.objects.filter(min_mthly_pay_in__lte=monthly_income,req_dd__lte=direct_debits,end_date__gte=today).order_by('end_date'):
            formatted_end_date = datetime.date.strftime(a.end_date, "%d/%m/%Y")
            formatted_start_date = datetime.date.strftime(a.start_date, "%d/%m/%Y")
            t = {
                'id':a.id,
                'bank':a.bank,
                'offer_title':a.offer_title,
                'switch_bonus':a.switch_bonus,
                'referral':a.referral,
                'min_mthly_pay_in':a.min_mthly_pay_in,
                'req_dd':a.req_dd,
                'extra_perks':a.extra_perks,
                'fees':a.fees,
                'fees_comment':a.fees_comment,
                'monthly_bonus':a.monthly_bonus,
                'monthly_bonus_cmt':a.monthly_bonus_cmt,
                'instructions':a.instructions,
                'monthly_interest':a.monthly_interest,
                'terms':a.terms,
                'offer_url':a.offer_url,
                'start_date':formatted_start_date,
                'end_date':formatted_end_date,     
            }
            offer_list.append(t)
            # print (f"URL: {a.offer_url} and Start Date: {a.start_date} Bank: {a.bank}")

        stuff_for_frontend = {
            'offer_list': offer_list,
            'monthly_income':monthly_income,
            'direct_debits':direct_debits,
            'money_saved':money_saved,
        }
        return render(request, 'my_app/new_search.html', stuff_for_frontend)
    else:
        stuff_for_frontend = {
            'error_message': "You have to fill out all fields.",
        }
        return render(request, 'my_app/new_search.html', stuff_for_frontend)


                # 'id':a.id,  
                # 'bank':a.bank,
                # 'switch_bonus':a.switch_bonus,
                # 'monthly_bonus':a.monthly_bonus,
                # 'monthly_interest':a.monthly_interest,
                # 'referral':a.referral,
                # 'min_mthly_pay_in':a.min_mthly_pay_in,
                # 'req_dd':a.req_dd,             
                # 'extra_perks':a.extra_perks,         
                # 'offer_url':a.offer_url,           
                # 'start_date':formatted_start_date,       
                # 'end_date':formatted_end_date, 
    
