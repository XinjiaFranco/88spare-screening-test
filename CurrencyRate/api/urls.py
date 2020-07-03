from django.urls import path
from .views import currency_list, currency_detail


urlpatterns = [
    path('currency/', currency_list),
    path('detail/<int:pk>', currency_detail),

]
