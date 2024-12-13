from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart, CartItem
from django.contrib import messages


def product_list(request):
    """Display a list of all products."""
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def home(request):
    """Render the home page with featured products and categories."""
    featured_products = Product.objects.filter(is_featured=True)
    categories = Category.objects.all()
    return render(
        request,
        "home.html",
        {"featured_products": featured_products, "categories": categories},
    )


def product_detail(request, product_id):
    """Render the product detail page for a specific product."""
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_detail.html", {"product": product})


def add_to_cart(request):
    """Add a product to the shopping cart."""
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)

        # Get or create a cart associated with the session
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(
            session_key=request.session.session_key
        )

        # Check if the product is already in the cart
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )
        if not item_created:
            cart_item.quantity += 1  # Increment quantity if already in cart
            cart_item.save()

        return redirect("view_cart")
    return redirect("home")


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
    return render(request, "cart.html", {"cart": cart})


def remove_from_cart(request, item_id):
    """Remove an item from the cart."""
    session_key = request.session.session_key
    if session_key:
        cart = Cart.objects.filter(session_key=session_key).first()
        if cart:
            cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
            cart_item.delete()
            messages.success(request, "Item removed from the cart.")
    return redirect("view_cart")


def checkout(request):
    """Handle the checkout process."""
    session_key = request.session.session_key
    if not session_key:
        return redirect("view_cart")  # Redirect if no cart exists

    cart = Cart.objects.filter(session_key=session_key).first()
    if not cart:
        return redirect("view_cart")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")

        # Basic validation
        if not name or not email or not address:
            messages.error(request, "All fields are required.")
            return render(request, "checkout.html", {"cart": cart})

        # Save order details (this can be expanded)
        # Clear the cart
        cart.items.all().delete()
        cart.delete()
        messages.success(request, "Thank you for your purchase!")
        return redirect("home")

    return render(request, "checkout.html", {"cart": cart})
