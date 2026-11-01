from django.shortcuts import render, get_object_or_404
from .models import Restaurant


def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(
        Restaurant,
        id = restaurant_id,
        is_active = True
    )
    food_items = restaurant.food_items.filter(
        is_available = True
    )
    return render(request, "restaurant_detail.html",{
        "restaurant":restaurant,
        "food_items":food_items
    })