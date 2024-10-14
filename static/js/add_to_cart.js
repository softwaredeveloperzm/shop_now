$(document).ready(function() {
    // Event listener for adding to cart
    $(document).on('click', "#addToCartBtn", function() {
        var $form = $(this).closest('form');
        var qty = $form.find('.product-qty').val();
        var productId = $form.find('.product-id').val();
        var productTitle = $form.find('.product-title').val();
        var productPrice = $form.find('.product-price').val();

        // AJAX request to add the product to the cart
        $.ajax({
            url: '/cart/add-to-cart/',
            data: {
                'id': productId,
                'qty': qty,
                'title': productTitle,
                'price': productPrice
            },
            success: function(response) {
                console.log('Response data: ', response);

                // Update the number of unique product titles in real-time
                $('#cartProductCount').text(response.total_unique_titles);
            },
            error: function(xhr, errmsg, err) {
                console.log('Error: ', errmsg);
            }
        });
    });

    // Fetch initial cart count on page load
    $.ajax({
        url: '/cart/get-cart-count/', // Endpoint to get the initial cart count
        success: function(response) {
            $('#cartProductCount').text(response.total_unique_titles);
        },
        error: function(xhr, errmsg, err) {
            console.log('Error: ', errmsg);
        }
    });
});
