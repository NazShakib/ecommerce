var cartUpdate = document.getElementsByClassName('update-cart')

for (var i = 0; i < cartUpdate.length; i++) {

    cartUpdate[i].addEventListener('click', function() {

        var productId = this.dataset.product
        var action = this.dataset.action
        if (user == "AnonymousUser") {

            addCookieItem(productId, action)

        } else {
            UpdateCart(productId, action)
        }

    })
}


function addCookieItem(productId, action) {
    // console.log("You are not logged in")

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = { 'quantity': 1 }
        } else {
            cart[productId]['quantity'] += 1
        }
    }
    if (action == 'remove') {
        cart[productId]['quantity'] -= 1
        if (cart[productId]['quantity'] <= 0) {
            console.log('Item removed')
            delete cart[productId]
        }

    }
    // console.log('cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    window.location.reload(true);
}

function UpdateCart(productId, action) {
    // console.log('product Id: ', productId, 'action: ', action)
    console.log("you are logged in")

    var url = "/update-data/"
    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })
    }).then(response => {
        return response.json()
    }).then(data => {
        console.log('data:', data)
        window.location.reload(true);
    })
}