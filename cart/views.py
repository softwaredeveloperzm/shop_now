from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from core.views import product_details


def add_to_cart(request):
    product_id = request.GET.get('id')
    qty = int(request.GET.get('qty'))
    title = request.GET.get('title')
    price = float(request.GET.get('price'))

    cart_data = request.session.get('cartdata', {})

    if product_id in cart_data:
        cart_data[product_id]['qty'] += qty
    else:
        cart_data[product_id] = {
            'id': product_id,
            'qty': qty,
            'title': title,
            'price': price
        }

    request.session['cartdata'] = cart_data

    total_unique_titles = len(cart_data)

    return JsonResponse({
        'total_unique_titles': total_unique_titles
    })


def get_cart_count(request):
    cart_data = request.session.get('cartdata', {})
    total_unique_titles = len(cart_data)

    return JsonResponse({
        'total_unique_titles': total_unique_titles
    })

def update_cart_qty(request):
    title = request.GET.get('title')
    action = request.GET.get('action')
    cart_data = request.session.get('cartdata', {})

    item_to_remove = None
    for item_id, item_data in cart_data.items():
        if item_data['title'] == title:
            if action == 'increment':
                cart_data[item_id]['qty'] += 1
            elif action == 'decrement' and cart_data[item_id]['qty'] > 1:
                cart_data[item_id]['qty'] -= 1
            elif action == 'decrement' and cart_data[item_id]['qty'] <= 1:
                item_to_remove = item_id

    if item_to_remove:
        del cart_data[item_to_remove]

    request.session['cartdata'] = cart_data

    total_qty = sum(item['qty'] for item in cart_data.values())
    total_price = sum(item['qty'] * float(item['price']) for item in cart_data.values())

    return JsonResponse({
        'total_qty': total_qty,
        'total_price': total_price,
        'cart_data': cart_data
    })

def review(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        product = request.POST.get("product-id")
  
        print(comment, product)

    return HttpResponse("Data sent")