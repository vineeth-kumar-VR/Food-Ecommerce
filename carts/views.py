from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from foods.models import Fooditems
from .models import Cart, Cartitems
from django.contrib import messages


@login_required
def add_to_cart(request, food_id):
    food = get_object_or_404(
        Fooditems,
        id = food_id,
        is_available = True
    )
    carts, created = Cart.objects.get_or_create(
        user = request.user
    )
    cart_item, created = Cartitems.objects.get_or_create(
        cart = carts,
        food = food,
        defaults={"quantity":1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = cart.items.select_related(
        'food'
    ).all()
    for item in cart_items:
        item.subtotal = item.food.price * item.quantity
    total = sum(item.subtotal for item in cart_items)

    return render(request, 'cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total': total,
    })
    
    
@login_required
def update_quantity(request,item_id,action):
    if request.method == "POST":
        cart = get_object_or_404(Cart, user = request.user)
        item = get_object_or_404(
            Cartitems,
            id = item_id,
            cart = cart
        )
        if action == "increase":
            item.quantity += 1
            item.save()
        elif action == "decrease":
            if item.quantity > 1:
                item.quantity -= 1
                item.save(update_fields=["quantity"])
            else:
                item.delete()
    return redirect("view_cart")

@login_required
def remove_from_cart(request, item_id):
    if request.method == "POST":
        cart = get_object_or_404(Cart, user = request.user)
        item = get_object_or_404(
            Cartitems,
            id = item_id,
            cart = cart
            
        )
        item.delete()
        messages.success(request, "Item removed from your cart!")
    return redirect("view_cart")
    