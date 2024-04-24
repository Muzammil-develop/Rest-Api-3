from django.urls import path
from .import views

urlpatterns = [
    path ('list' , views.pant_view.as_view() , name= 'pant_list'),
    path ('<int:pk>' , views.pant_detail_view.as_view () , name='pant_detail'),
    path ('store' , views.store_view.as_view() , name= 'store_list'),
    path ('store/<int:pk>' , views.store_detail_view.as_view () , name='store_detail'),
]

