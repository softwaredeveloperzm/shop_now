from cart.models import CartItems


def get_cart_count(request):
    cart_count = 0

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Fetch cart items from the database for the logged-in user
        cart_count = CartItems.objects.filter(user=request.user).count()
    else:
        # Fetch cart items from the session for an anonymous user
        cart = request.session.get('cart', [])
        cart_count = len(cart)
    
    return cart_count
