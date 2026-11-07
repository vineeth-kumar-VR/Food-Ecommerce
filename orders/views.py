
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from carts.models import Cart
from .models import Order, Address, OrderItem


@login_required
def checkout(request):

    # Get the logged-in user's cart
    cart = Cart.objects.filter(user=request.user).first()

    if not cart or not cart.items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')

    # Get cart items
    cart_items = cart.items.select_related(
        'food', 'food__restaurant'
    ).all()

    # Check whether cart contains food from multiple restaurants
    restaurants = {
        item.food.restaurant_id for item in cart_items
    }

    if len(restaurants) > 1:
        messages.warning(
            request,
            "Please order from one restaurant at a time."
        )
        return redirect('view_cart')

    # Calculate total amount
    total = sum(
        (
            item.food.price * item.quantity
            for item in cart_items
        ),
        Decimal('0.00')
    )

    # Get user's saved addresses
    addresses = Address.objects.filter(user=request.user)

    if request.method == 'POST':

        address_id = request.POST.get('address')

        address = Address.objects.filter(
            id=address_id,
            user=request.user
        ).first()

        if not address:
            messages.error(
                request,
                "Please select a valid address."
            )
            return redirect('checkout')

        # Get restaurant from first cart item
        first_item = cart_items[0]

        # Create order
        order = Order.objects.create(
            user=request.user,
            restaurant=first_item.food.restaurant,
            address=address,
            total_amount=total,
            status='pending'
        )

        # Create order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                food=item.food,
                quantity=item.quantity,
                price=item.food.price
            )

        cart_items.delete()

        messages.success(
            request,
            "Your order has been placed successfully!"
        )

        return redirect('view_cart')

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'addresses': addresses,
    })

@login_required
def add_to_address(request):
    if request.method == "POST":
        address = request.POST.get("address")
        city = request.POST.get("city")
        pincode = request.POST.get("pincode")
        phone = request.POST.get("phone")
        if not all([address, city, pincode, phone]):
            messages.error(request, "Please fill all the fields")
            return redirect("address")
        Address.objects.create(
            user = request.user,
            address = address,
            city = city,
            pincode = pincode,
            phone = phone
            
        )
        messages.success(request, "Address Added Successfully")
        return redirect("checkout")
    return render(request, "address.html")

@login_required
def my_order(request):
    print("logged_in_user:", request.user, request.user.id)

    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related(
        'items__food'
    ).order_by('-created_at')

    print("order_count:", orders.count())

    return render(request, 'my_order.html', {
        'orders': orders
    })
    
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(
        Order,
        id = order_id,
        user =request.user
    )
    return render(request, "order_detail.html",{
        "order":order
    })
    