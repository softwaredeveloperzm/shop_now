from django.urls import path
from django.conf import settings
from cart import views


urlpatterns = [
    
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'), 
    path('update-cart-qty/', views.update_cart_qty, name='update-cart-qty'),
    path('get-cart-count/', views.get_cart_count, name='get_cart_count'),
    path('review/', views.review, name="review"),

]
