from django.urls import path
from .import views

urlpatterns = [
    path('', views.flight_form, name='flight_form'),
    path('get_items/',views.get_items,name='get_items'),
    path('create_flight/',views.create_flight,name='create_flight'),
    path('search_flight/', views.search_flight, name='search_flight')

]