from django.urls import path
from . import views
urlpatterns = [
    path("add/<int:food_id>", views.add_to_cart, name="add_to_cart"),
    path("", views.view_cart, name="view_cart"),
    path("update/<int:item_id>/<str:action>", views.update_quantity, name="update_quantity"),
    path("remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart")
]
