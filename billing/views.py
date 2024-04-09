from django.conf import settings 
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.utils.http import url_has_allowed_host_and_scheme as is_safe_url

from .models import BillingProfile, Card
# Create your views here.
import stripe
STRIPE_SECRET_KEY= getattr(settings,"STRIPE_SECRET_KEY","sk_test_51ORg5RSHlQBXvLgggewVG7tPoP76c9OETtmLrsYnRQMLdHr3x8YZlbwYcewKQsYLzPhzHDpMcMP4Wq89reUyLC0G00hC3AX3Um")
STRIPE_PUB_KEY= getattr(settings,"STRIPE_PUB_KEY","pk_test_51ORg5RSHlQBXvLggpCUGcViFkvLvrld6sqBudj9ONHqFY6GhHX5o7TRsfVlM7jQk2y98qBSARZYuUZL9obkVtaHs00FEzlrubf")
stripe.api_key = STRIPE_SECRET_KEY

def payment_method_view(request):
	#if request.user.is_authenticated():
	#	billing_profile = request.user.billingprofile
	#	my_customer_id = billing_profile.customer_id

	billing_profile, billing_profile_created  =   BillingProfile.objects.new_or_get(request)
	if not billing_profile:
		return redirect("/cart")

	next_url=None
	next_=request.GET.get('next')
	if is_safe_url(next_, request.get_host()):
		next_url=next_
		

	return render(request,'billing/payment-method.html',{"publish_key":STRIPE_PUB_KEY,"next_url":next_url})

def payment_method_createview(request):
	if request.method=="POST" and request.is_ajax():
		billing_profile, billing_profile_created  =   BillingProfile.objects.new_or_get(request)
		if not billing_profile:
			return HttpResponse({"message": "Cannot find this user"},status_code=401)
		token = request.POST.get("token")
		if token is not None:
			#customer = stripe.Customer.modify(billing_profile.customer_id, source=token)
			new_card_obj = Card.objects.add_new(billing_profile, token)
			print(new_card_obj)   #start saving our cards too!

		return JsonResponse({"message":"Success! card added "})
	return HttpResponse("error", status_code=401)