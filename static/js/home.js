$(document).ready(function() {
    // Function to set a cookie
    function setCookie(name, value, days) {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
    }

    // Function to get a cookie
    function getCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    // Function to update the cart value in the navigation bar
    function updateCartValue() {
        var cart = JSON.parse(getCookie('cart') || '[]');
        var totalItems = cart.reduce((total, item) => total + item.quantity, 0);
        $('.cart-value').text(totalItems);
    }

    // Function to update the cart in cookies
    function updateCart(cart) {
        setCookie('cart', JSON.stringify(cart), 7);
        updateCartValue();
    }

    // Function to update the displayed cart items
    function updateCartDisplay() {
        var cart = JSON.parse(getCookie('cart') || '[]');
        var total_price = 0;
        cart.forEach(function(item) {
            var itemTotalPrice = item.price * item.quantity;
            total_price += itemTotalPrice;
            var cartItem = $('.cart-item[data-product-id="' + item.id + '"]');
            cartItem.find('.item-quantity').text(item.quantity);
            cartItem.find('.item-total-price').text('$' + itemTotalPrice.toFixed(2));
        });
        $('.cart-total-price').text('$' + total_price.toFixed(2));
    }

    // Initial update of the cart value on page load
    updateCartValue();
    updateCartDisplay();

    // Event listener for add-to-cart button
    $('.add-to-cart-btn').on('click', function(e) {
        e.preventDefault();
        var productId = $(this).data('product-id');
        var productTitle = $(this).data('product-title');
        var productPrice = $(this).data('product-price');
        var productQuantity = 1; // Default quantity is 1

        // Retrieve the cart from cookies or initialize it
        var cart = JSON.parse(getCookie('cart') || '[]');

        // Check if the product is already in the cart
        var productExists = cart.some(function(item) {
            return item.id === productId;
        });

        if (!productExists) {
            // Add the product to the cart
            cart.push({
                id: productId,
                title: productTitle,
                price: productPrice,
                quantity: productQuantity
            });
            updateCart(cart);
            console.log('Product "' + productTitle + '" added to cart.');
        } else {
            console.log('Product "' + productTitle + '" is already in the cart.');
        }

        // Log all items in the cart
        console.log('Cart items:', cart);
    });

    // Event listeners for increment and decrement buttons
    $(document).on('click', '.btn-increment', function() {
        var productId = $(this).data('product-id');
        var cart = JSON.parse(getCookie('cart') || '[]');

        cart = cart.map(function(item) {
            if (item.id === productId) {
                item.quantity += 1;
            }
            return item;
        });

        updateCart(cart);
        updateCartDisplay(); // Update the cart display without refreshing the page
    });

    $(document).on('click', '.btn-decrement', function() {
        var productId = $(this).data('product-id');
        var cart = JSON.parse(getCookie('cart') || '[]');

        cart = cart.map(function(item) {
            if (item.id === productId && item.quantity > 1) {
                item.quantity -= 1;
            }
            return item;
        });

        updateCart(cart);
        updateCartDisplay(); // Update the cart display without refreshing the page
    });
});
