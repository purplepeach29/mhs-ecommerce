

from django.urls import re_path as url


from .views import (SearchProductView)

urlpatterns = [
   
    url(r'^$',SearchProductView.as_view(),name='query'),
   	#url(r'^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(),name='detail'),
 
]

 