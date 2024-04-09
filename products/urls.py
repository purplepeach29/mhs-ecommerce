

from django.urls import re_path as url


from .views import (ProductListView,ProductDetailSlugView,)

urlpatterns = [
   
    url(r'^$',ProductListView.as_view(),name='list'),
   	url(r'^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(),name='detail'),
 
]

 