from django.urls import path
from .views import home, contact, sobre


urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('sobre/', sobre),
]
