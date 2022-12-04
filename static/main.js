console.log("Sanity check!");

// Get Stripe publishable key
// fetch("config/")
fetch("http://localhost:8000/customer_portal/config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", (e) => {
    e.preventDefault;
    // Get Checkout Session ID
    fetch("http://localhost:8000/customer_portal/create-checkout-session/")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});
