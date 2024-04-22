from django.urls import path

from .views import *

urlpatterns = [
    path('registration/',  User_RegistrationCreateView.as_view() , name = 'registration'),
    path('customer_profile/<slug:slug>/', CustomerProfileRetrieveView.as_view(), name='customer_profile'),
    path('performer_pofile/<slug:slug>/', PerformerProfileRetrieveView.as_view(), name='performer_pofile'),
    path('search_vacancy/', SearchVacancyListView.as_view(), name='search_vacancy'),

]