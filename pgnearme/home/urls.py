from django.urls import path
from . import views
from home import views
from .views import *


urlpatterns = [
    path('', views.index, name='home'),
    # path("about", views.about, name="about"),
    path('contact/', views.contact, name='contact'),
    path("", views.home, name='home'),
]