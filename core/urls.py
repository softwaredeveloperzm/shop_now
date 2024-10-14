from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_details/<int:id>', views.product_details, name='product_details'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('search_products', views.search_products, name='search_products'),
    path('process_transaction', views.process_transaction, name='process_transaction'),
    path('transaction_complete/', views.transaction_complete, name='transaction_complete'),
    path('transaction_fail/', views.transaction_fail, name='transaction_fail'),
    path('buy_now/<int:id>', views.buy_now, name='buy_now'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
