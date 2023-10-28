let forms = document.querySelectorAll(".cart-add-form");

forms.forEach((form) => {
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        let formData = new FormData(this);

        fetch(this.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
            },
        })
            .then((response) => response.json())
            .then((data) => {
                const cartItemsCounter = document.querySelector(
                    "#cart-items-counter"
                );
                cartItemsCounter.textContent = data.cartItemsCount;
                
                if (data.message) {
                    alert(data.message);
                }
            })
            .catch((error) => {
                console.error(error);
            });
    });
});
