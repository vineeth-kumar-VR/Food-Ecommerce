from django.urls import path
from . import views

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("address/", views.add_to_address, name="add_to_address"),
    path("my_order/", views.my_order, name="my_order"),
    path("order_detail/<int:order_id>/", views.order_detail, name="order_detail")
]
