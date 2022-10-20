var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card');
card.mount("#card-element");

// Set up Stripe.js and Elements to use in checkout form
var elements = stripe.elements();
var style = {
  base: {
    color: "#32325d",
  }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");


// handle errors

// card.addEventListener('change', function (event){
//   var errorDiv = document.getElementById('card-errors');
//   if (event.error){
//     var html =
//       <span>${event.error.message}</span>
//     $(errorDiv).html(html);
//   } else{
//     errorDiv.textContent = '';
//   }
// });


// handle submit

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({'disabled': true});
  $('#submit-button').attr('disabled',true);
  $('#payment-form').fadeToggle(100);
  $('#loading-overlay').fadeToggle(100);
  // If the client secret was rendered server-side as a data-secret attribute
  // on the <form> element, you can retrieve it here by calling `form.dataset.secret`
  console.log(clientSecret)
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function(result) {
    if (result.error) {
      // Show error to your customer (for example, insufficient funds)
      console.log(result.error.message);
      card.update({'disabled': false});
      $('#payment-form').fadeToggle(100);
      $('#loading-overlay').fadeToggle(100);
      $('#submit-button').attr('disabled',false);
    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
          form.submit();
      }
    }
  });
});