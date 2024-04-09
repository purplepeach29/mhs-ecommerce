from django.contrib.auth import authenticate, login,get_user_model
from django.shortcuts import redirect,render
from django.http import HttpResponse,JsonResponse
from accounts.forms import LoginForm,RegisterForm
from .forms import ContactForm
def home_page(request):

	#print(request.session.get("first_name","unknown"))
	context={
	"title":"home page"
	}
	if request.user.is_authenticated:
		context["premium_content"]="yeahh"
	return render(request,"home_page.html",context)
 
def contact_page(request):
	contact_form=ContactForm(request.POST or None)
	context={
	#"title": "Tell us how you feel",
	"form":contact_form
	}
	
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
		if request.is_ajax():
	 		return JsonResponse({"message":"Thank You"})
	if contact_form.errors:
		errors=contact_form.errors.as_json()
		if request.is_ajax():
	 		return HttpResponse(errors,status=400,content_type='application/json')
	
	# if request.method=="POST":
	# 	print(request.POST)
	return render(request,"contact/view.html",context)

def home_page_old(request):
	html_="""
		<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
  <div class ='text-center'>
  		<h1>prachi<h1>
  		</div>

    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>

	"""
	return HttpResponse(html_)