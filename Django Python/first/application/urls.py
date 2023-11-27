from django.contrib import admin
from django.urls import path
from application import views
from django.shortcuts import HttpResponse

urlpatterns = [
    path('',views.home,name="Home"),
    path('about',views.about,name="About"),
    path('services',views.services,name="Services"),
    path('additional_information',views.additional_information,name="additional_information"),
    path('contact',views.contact,name="Contact Us"),
    path('additional_information/', views.text_to_speech, name='text_to_speech'),
    path('favicon.ico', lambda x: HttpResponse(status=204)),
]