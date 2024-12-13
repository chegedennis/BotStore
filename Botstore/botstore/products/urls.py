from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path(
        "<int:product_id>/", views.product_detail, name="product_detail"
    ),  # Change this line
    path("cart/add/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("product/checkout/", views.checkout, name="checkout"),
]
