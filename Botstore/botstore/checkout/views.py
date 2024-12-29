from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem
from django.contrib import messages
import requests  # Ensure requests is imported for API calls
import stripe  # Ensure stripe is imported for payment processing


def product_list(request):
    """Display a list of all products."""
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def view_cart(request):
    """Display the user's cart."""
    session_key = request.session.session_key
    if not session_key:
        return render(
            request, "cart.html", {"cart": None, "message": "Your cart is empty."}
        )
    cart = Cart.objects.filter(session_key=session_key).first()
    if not cart:
        return render(
            request, "cart.html", {"cart": None, "message": "Your cart is empty."}
        )
    cart_items = cart.cartitem_set.all()  # Retrieve all items in the cart
    return render(request, "cart.html", {"cart": cart, "cart_items": cart_items})


def checkout(request):
    """Handle the checkout process."""
    session_key = request.session.session_key  # Retrieve the session key
    if not session_key:
        return redirect("view_cart")  # Redirect if no cart exists

    cart = Cart.objects.filter(session_key=session_key).first()
    if not cart:
        return redirect("view_cart")

    if request.method == "POST":
        payment_method = request.POST.get("payment_method")
        email = request.POST.get("email")

        # Debugging output
        print(f"Session Key: {session_key}, Cart: {cart}")

        if payment_method == "stripe":
            token = request.POST.get("stripeToken")  # Get the token from the form
            try:
                charge = stripe.Charge.create(
                    amount=int(total_cost * 100),  # Amount in cents
                    currency="usd",
                    description="Payment for products",
                    source=token,
                    receipt_email=email,
                )
                # Make an API call to complete the purchase
                api_url = "https://your-api-endpoint.com/complete-purchase"  # Replace with actual API endpoint
                purchase_data = {
                    "email": email,
                    "cart_items": cart.cartitem_set.all(),
                    "total_cost": total_cost,
                    "payment_method": payment_method,
                }
                api_response = requests.post(api_url, json=purchase_data)

                if api_response.status_code == 200:
                    messages.success(
                        request, "Payment processed successfully and purchase completed"
                    )
                    # Clear the cart
                    cart.cartitem_set.all().delete()
                    cart.delete()
                    return redirect("home")
                else:
                    messages.error(request, "Failed to complete the purchase")
            except stripe.error.StripeError as e:
                messages.error(request, str(e))

    return render(request, "checkout.html", {"cart": cart})
