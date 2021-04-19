from django.urls import path
from . import views

urlpatterns = [
    path('',views.bakery_list, name='bakery_list'),
    path('about',views.about, name='about'),
]
