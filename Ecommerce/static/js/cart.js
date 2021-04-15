var btnUpdate = document.getElementsByClassName('update-cart');

for(var i=0; i<btnUpdate.length; i++) {
	btnUpdate[i].addEventListener('click', function() {
		var productID = this.dataset.product;
		var action = this.dataset.action
		console.log(productID, action)

		console.log("USER", user)
		if (user === 'AnonymousUser') {
			console.log("Error")
		} else {
			updateUserOrder(productID, action)
		}
	})
}

function updateUserOrder(productID, action) {
	console.log("Sending")

	var url = '/updateitem/'

	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body: JSON.stringify({'productID': productID, 'action': action})
	})

	.then((response) => {
		return response.json();
	})

	.then((data) => {
		console.log('data: ', data)
	})
}