// static/js/update_cart_quantity.js

$(document).ready(function() {
    $(document).on('click', '#updateQty', function() {
        var $form = $(this).closest('form');
        var productTitle = $form.find('.item-title').val();
        var action = $(this).data('action');

        $.ajax({
            url: '/cart/update-cart-qty/',
            data: {
                'title': productTitle,
                'action': action
            },
            success: function(response) {
                // Check if the product exists in the response
                var item = Object.values(response.cart_data).find(item => item.title === productTitle);

                if (item) {
                    // Update item details
                    $('#itemQty_' + productTitle).text(item.qty);
                    $('#itemTotal_' + productTitle).text('K' + (item.qty * parseFloat(item.price)).toFixed(2) + '.00');
                } else {
                    // Remove item from DOM if it doesn't exist
                    $('#itemQty_' + productTitle).closest('.card').remove();
                }

                // Update total quantity and price
                $('#totalQty').text(response.total_qty);
                $('#totalPrice').text('K' + response.total_price.toFixed(2) + '.00');
            },
            error: function(xhr, errmsg, err) {
                console.log('Error: ', errmsg);
            }
        });
    });
});
