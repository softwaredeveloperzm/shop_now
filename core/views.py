from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Product, Order
from .utils import get_cart_count
from cart.models import Review
import json
import time

def home(request):

    start_time = time.time()

    cart_count = get_cart_count(request)
    products = Product.objects.all()

   

    context = {
        'products' : products,
        'cart_count' : cart_count,
    }

    total = time.time() - start_time

    print(total)
    return render(request, 'core/home.html', context)

def product_details(request, id):
    start_time = time.time()
    product_details = get_object_or_404(Product, id=id)
    if Review.objects.filter(product = product_details).exists():
        reviews = get_object_or_404(Review, product = product_details)
     
        comment = reviews.comment
        user = reviews.user
        date = reviews.created_at

        
    
    else:

        print("Does not")

    context = {
        'product_details': product_details,
        'user': user,
        'comment': comment,
        'date': date, 

    }
    
    total = time.time() - start_time

    print(total)
    return render(request, 'core/product_details.html', context)


from django.shortcuts import get_object_or_404
from core.models import Product

def get_cart_data(request):
    # Retrieve cart from session or initialize as an empty dictionary
    cart = request.session.get('cartdata', {})

    items = []
    total_price = 0  # Initialize total price

    # Iterate over the cart dictionary
    for item_id, item_data in cart.items():
        # Access the title using dictionary-style access
        id = item_data.get('id')
        title = item_data.get('title', 'No title')
        product = get_object_or_404(Product, title=title)

        image = product.image.url
        price = product.price
        qty = item_data.get('qty', 1)  # Default to 1 if qty not found

        # Calculate the total price for the product
        final_price_product = price * qty

        # Accumulate the total price for the cart
        total_price += final_price_product

        # Append the item details to the items list
        items.append({
            'id':  id,
            'title': title,
            'price': price,
            'image': image,
            'qty': qty,
            'final_price_product': final_price_product,
        })

    context = {
        'items': items,
        'total_price': total_price,  # Include total price in the context
    }

    return items, total_price


def cart(request):
    start_time = time.time()
    items, total_price  = get_cart_data(request)

    context = {
        'total_price': total_price,
        'items': items
    }
    
    total = time.time() - start_time

    print(total)
   

    return render(request, 'core/cart.html', context)



def checkout(request):
    items, total_price = get_cart_data(request)

    context = {
        'items': items,
        'total_price': total_price,
    }
    
    return render(request, 'core/checkout.html', context)


def buy_now(request, id):

    product = Product.objects.filter(id=id)
    items = []
    
    for item in product:
        price = item.price
        title = item.title
        image = item.image.url

        items.append({
            'price': price,
            'title': title,
            'image': image


        })

    context = {
        'items': items,
    }
    return render(request, 'core/buy_now.html', context)

def login(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        user = authenticate(username=user_email, password=user_password)
        if user is not None:
            auth_login(request, user)  
            return redirect('home')  
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')  

    return render(request, 'core/login.html')


def register(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_confrim_password = request.POST.get('confrim_password')

        
        if User.objects.filter(username=user_email).exists():
            messages.info(request, 'Email Already Taken')
            return redirect(register)
        
        elif user_password != user_confrim_password:
            messages.warning(request, 'Password Does Not Match!')
            return redirect(register)

        else:
            create_user = User.objects.create_user(username=user_email, password=user_password)

            messages.info(request, 'Account created succesfully!')
            return redirect(login)

    return render(request, 'core/register.html')


def logout_user(request):
    auth_logout(request)
    return redirect(home)


def search_products(request):
    if request.method == 'POST':
        query = request.POST.get('search_query')
        products = Product.objects.filter(title__contains=query)
        context = {
            'products': products
        }


    return render(request, 'core/search_results.html', context)

@csrf_exempt
def process_transaction(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            transaction_id = data.get('id', '')
            items = data.get('items', [])
            total_price = data.get('total_price', '')

            order = Order.objects.create(transaction_id=transaction_id, total_price=total_price)
            
            return JsonResponse({'status': 'success'})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'failure', 'message': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'status': 'failure', 'message': 'Invalid request method'}, status=400)

def transaction_complete(request):
    return render(request, 'core/transaction_complete.html')

def transaction_fail(request):
    return render(request, 'core/transaction_fail.html')


