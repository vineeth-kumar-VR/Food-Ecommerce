from django.urls import path
from . import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("address/", views.add_to_address, name="add_to_address")
]
