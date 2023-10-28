function toggleTheme() {
    const html = document.querySelector("html");
    html.classList.toggle("dark");
}

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
                if (data.message) {
                    alert(data.message);
                }
            })
            .catch((error) => {
                console.error(error);
            });
    });
});
