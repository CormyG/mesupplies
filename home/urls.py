from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name= 'home'),
    
]

handler404 = "home.views.page_not_found_view"