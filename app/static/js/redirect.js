document.write("wqeqwe");
        console.getElementById('buyButton').addEventListener('click', function() {
            fetch(`/buy/{{ item.id }}`)
                .then(response => response.json())
                .then(data => {
                    var stripe = Stripe("sk_test_51Ns7wcBwJOVg17VQaFqrT6dFeVfP7uru9qSZczDKpH9buthbg4J2fI24YpoaXArtSwnB4hH1D4baHZebTSNSIy1a00LGXiixbQ");
                    console.log(data.session_id)
                    stripe.redirectToCheckout({ sessionId: data.session_id });
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
