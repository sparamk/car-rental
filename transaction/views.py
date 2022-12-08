from django.shortcuts import render
from booking.views import *
from car.models import *
from booking.models import *
from owner.models import *
from django.http import JsonResponse
import stripe
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
# import stripe

# Create your views here.
def payment(request):
    bookings = Book.objects.all()
    booked_cars = Book_Car.objects.all()
    booking_list = []
    for booking in bookings:
        if (booking.confirmation == 1 and booking.is_paid == 0):
            booked_car = Book_Car.objects.filter(id=booking.book_car_id)
            # car = Cars.objects.filter(id=booking.book_car_id)
            # booking_list_dictionary = {
            #     'from_date':booking.from_date,
            #     'to_date':booking.to_date,
            #     'rent':booked_car.id,
            #     # 'car_name':car.car_name,
            #     }
            # booking_list.append(booking_list_dictionary)
    return render(request, 'payment.html',{'bookings':booked_car})



def applyCoupon(request):
    if request.method == 'POST':
        coupons = Coupons.objects.filter(coupon_code=request.POST['data'])
        exist = Coupons.objects.filter(coupon_code=request.POST['data']).exists()
        return JsonResponse({"coupons":list(coupons.values()),'exist':exist})


    
# below are the four methods being used frmo the stripe api into the transactions app

class SuccessView(TemplateView):
    template_name = 'checkout/success.html'

def success(request):
    if request.method == 'GET':
        success = request.GET['session_id']
        return render(request, 'checkout/success.html',{'success':success})

class CancelledView(TemplateView):
    template_name = 'checkout/cancelled.html'


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        rent = request.GET['rent']
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                # client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'transaction/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'transaction/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'Rent',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': rent,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    # Stripe CLI setup + login
    # The easiest way to test our webhook is to download Stripe CLI (https://stripe.com/docs/stripe-cli)
    # After downloading it we need to login by running 'stripe login' in Terminal, this command will generate
    # a pairing code for us an open our web browser.
    #
    # ---------------------------------------------------------------
    # Your pairing code is: word1-word2-word3-word4
    # This pairing code verifies your authentication with Stripe.
    # Press Enter to open the browser (^C to quit)
    # ---------------------------------------------------------------
    #
    # By pressing enter CLI opens our browser and asks us if we want to allow Stripe CLI to access our account
    # information. We can allow it by clicking 'Allow access' button and confirming the action with our password.
    #
    # If everything goes well Stripe CLI will display the following message:
    #
    # ---------------------------------------------------------------
    # > Done! The Stripe CLI is configured for {ACCOUNT_NAME} with account id acct_{ACCOUNT_ID}
    # Please note: this key will expire after 90 days, at which point you'll need to re-authenticate.
    # ---------------------------------------------------------------
    #
    # Webhook setup
    # Once we successfully logged in we can start listening to Stripe events and forward them to our webhook using
    # the following command:
    #
    # stripe listen --forward-to localhost:8000/webhook/
    #
    # This will generate a webhook signing secret that we should save in our settings.py. After that we will
    # need to pass it when constructing a Webhook event.
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # This method will be called when user successfully purchases something.
        handle_checkout_session(session)

    return HttpResponse(status=200)


def handle_checkout_session(session):
    # client_reference_id = user's id
    client_reference_id = session.get("client_reference_id")
    payment_intent = session.get("payment_intent")

    if client_reference_id is None:
        # Customer wasn't logged in when purchasing
        return

    # Customer was logged in we can now fetch the Django user and make changes to our models
    try:
        user = User.objects.get(id=client_reference_id)
        print(user.username, "just purchased something.")

        # TODO: make changes to our models.

    except User.DoesNotExist:
        pass
