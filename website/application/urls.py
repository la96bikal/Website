from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home, name = "home"),
    path('other_page', views.other_page, name ="other_page"),
    path('ajax_processor', views.ajax_processor, name = "ajax_processor")
    ]


