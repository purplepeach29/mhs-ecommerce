from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.
class SearchProductView(ListView):
	#queryset=Product.objects.all()
	template_name="search/view.html"

	def get_context_data(self,*args,**kwargs):
		context=super(SearchProductView,self).get_context_data(*args,**kwargs)
		query=self.request.GET.get('q')
		context['query']=query
		return context

	def get_queryset(self,*args,**kwargs):
		request=self.request
		#print(request.GET)
		method_dict=request.GET
		query=method_dict.get('q',None)
		print(query)
		if query is not None:
			
			return Product.objects.search(query)
		return Product.objects.featured()