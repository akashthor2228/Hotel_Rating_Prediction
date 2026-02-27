const form = document.getElementById("predictForm");
const resultBox = document.getElementById("result");
const ratingText = document.getElementById("rating");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        avg_cost: document.getElementById("avg_cost").value,
        table_booking: document.getElementById("table_booking").value,
        online_delivery: document.getElementById("online_delivery").value,
        delivering_now: document.getElementById("delivering_now").value,
        price_range: document.getElementById("price_range").value,
        votes: document.getElementById("votes").value
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    ratingText.innerText = result.rating;
    resultBox.classList.remove("hidden");
});
