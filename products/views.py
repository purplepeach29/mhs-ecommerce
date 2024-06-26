from django.views.generic import ListView,DetailView
from django.shortcuts import render

from analytics.mixins import ObjectViewedMixin 
from .models import Product
from django.http import Http404 
from carts.models import Cart
# Create your views here.



class ProductFeaturedListView(ListView):
	#queryset=Product.objects.all()
	template_name="products/list.html"

	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.all().featured()


class ProductFeaturedDetailView(ObjectViewedMixin, DetailView):
	queryset=Product.objects.featured()
	template_name="products/featured-detail.html"
	"""def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.featured()"""


class ProductListView(ListView):
	template_name="products/list.html"

	#def get_context_data(self ,*args,**kwargs):
	#	context=super(ProductListView,self).get_context_data(*args,**kwargs)
	#	print(context)
	#	return context
	def get_context_data(self,*args,**kwargs):
		context=super(ProductListView,self).get_context_data(*args,**kwargs)
		
		cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		context['cart']=cart_obj
		return context

	def get_queryset(self,*args,**kwargs):
		request=self.request
		return Product.objects.all()


def product_list_view(request):
	queryset=Product.objects.all()
	context={'object_list':queryset
		}
	return render(request,"products/list.html",context)

class ProductDetailSlugView(ObjectViewedMixin, DetailView):
	queryset=Product.objects.all()
	template_name="products/detail.html"

	def get_context_data(self,*args,**kwargs):
		context=super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
		
		cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		context['cart']=cart_obj
		return context

	def get_object(self,*args,**kwargs):
		request=self.request
		slug=self.kwargs.get('slug')

		try:
			instance=Product.objects.get(slug=slug,active=True)
		except Product.DoesNotExist:
			raise Http404("DoesNotExist")
		except Product.MultipleObjectsReturned:
			qs=Product.objects.filter(slug=slug,active=True)
			instance=qs.first()
		except:
			raise Http404("hjgj")
		return instance


class ProductDetailView(ObjectViewedMixin, DetailView):
	queryset=Product.objects.all()
	template_name="products/detail.html"

	def get_context_data(self,*args,**kwargs):
		context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
		print(context)
		return context

	def get_object(self,*args,**kwargs):
		request=self.request
		pk=self.kwargs.get('pk')
		instance=Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("DoesNotExist")
		return instance


def product_detail_view(request,pk=None,*args,**kwargs):
	
	#queryset=Product.objects.all()
	#object=Product.object.get(all()
	#instance=get_object_or_404(Product,pk=pk)
	"""try:
		instance=Product.objects.get(id=pk)
	except Product.DoesNotExist:
		print('no product')
		raise Http404("product DoesNotExist")
	except:

		print('hih')"""
	
	instance=Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404(" DoesNotExist")
	"""print(instance)
	qs=Product.objects.filter(id=pk)
	if qs.exists() and qs.count()==1:
		instance=qs.first()
	else:
		raise Http404("DoesNotExist")"""
	context={
	'object':instance
	}
	return render(request,"products/detail.html",context)