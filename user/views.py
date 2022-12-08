from django.shortcuts import render, redirect
from customer.views import *
from . models import *
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage, send_mail
from pushpakcarrental import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
import math
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from . import tokens
from booking.views import *
from . tokens import generate_token
import secrets
import string
from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.admin import helpers
# from .helpers import send_forget_password_mail
# this is the default template for the app
def home(request):
    return render(request, 'authentication/index.html')

def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if len(password) == 0:
            messages.error(request, 'Password field cannot be null!')
            return render(request, 'authentication/signup.html')

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exists. Please choose a different Username!')
            return render(request, 'authentication/signup.html')

        if User.objects.filter(email=email):
            messages.error(request, 'Email already registered. Please use a different email!')
            return render(request, 'authentication/signup.html')

        if len(username) > 10:
            messages.error(request, 'Username must be under ten characters')
            return render(request, 'authentication/signup.html')
        
        if password != confirm_password:
            messages.error(request, 'Please enter the same password in both the password fields')
            return render(request, 'authentication/signup.html')
        
        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-Numeric')
            return render(request, 'authentication/signup.html')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.email = email
        myuser.is_active= False
        myuser.save()
        doser = myuser
        mygroup = Group.objects.get(name='customer')
        mygroup.user_set.add(doser)
        mygroup = Group.objects.get(name='ban')
        mygroup.user_set.remove(doser)
        messages.success(request, "Your account has been created successfully!")
        # Welcome Email
        subject = "Welcome to Pushpak Travels"
        message = "Hello "+first_name+"!! \n "+ "Welcome to Pushpak Travels \n Thankyou for using our services. Please check your mail for confirmation email. \n Please confirm your email address.\n\n Regards \n Admin"
        from_email = settings.EMAIL_HOST
        to_list = [email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        # Confirmation email
        current_site = get_current_site(request)
        email_subject = "Confirm Your Email | Pushpak Travels"
        email_message = render_to_string('email_confirmation.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })

        email = EmailMessage(
            email_subject,
            email_message,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        return render(request, 'authentication/login.html')

    return render(request, 'authentication/signup.html')

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        auth.login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect(login)
    else:
        messages.success(request, "Activation failed!!")
        return render(request,'authentication/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            request.session['customer'] = user.groups.filter(name='customer').exists()
            request.session['employee'] = user.groups.filter(name='employee').exists()
            request.session['manager'] = user.groups.filter(name='manager').exists()
            request.session['owner'] = user.groups.filter(name='owner').exists()
            # return redirect(dashboard)
            return redirect(modifyProfile)
        else:
            messages.error(request, "Bad credentials")
            return render(request, 'authentication/login.html')

    return render(request, 'authentication/login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def contactUs(request):
    return render(request, 'contactUs.html')


@login_required
def suggestRoadTrip(request):
    return render(request, 'suggestRoadTrip.html')


@login_required
def modifyProfile(request):
    old_username = request.user
    if request.method == 'POST':
        username1 = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        
        if User.objects.exclude(username=old_username).filter(username=username1).exists():
            error = "Username already exists. Please select a different Username"
            return render(request, 'modifyprofile.html', {
                "username":username1,
                "first_name":first_name,
                "last_name":last_name,
                }, {'error':error}) 
        else:
            user = User.objects.get(username = old_username.username)
            user.username = username1
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            success = "Data successfully changed"
        return render(request, 'modifyprofile.html', {
            "username":user,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "email":user.email,
            'success':success}) 
    else:
        user_id = request.user.id
        user = User.objects.get(id = user_id)
        return render(request, 'modifyprofile.html', {
            "username":user,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "email":user.email,
            })

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if not User.objects.filter(email=email):
            messages.error(request, "A User with this email is not found")
            return render(request, 'authentication/forgotpassword.html')
        myuser = User.objects.filter(email=email).first()
        myuser.is_active = False
        myuser.save()
        # Confirmation email
        current_site = get_current_site(request)
        email_subject = "Reset Your Email | Pushpak Travels"
        email_message = render_to_string('email_forgot_password.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })

        email = EmailMessage(
            email_subject,
            email_message,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()
        messages.success(request, "An email has been sent to reset the password")
        return render(request, 'authentication/forgotpassword.html')

    return render(request, 'authentication/forgotpassword.html')

def changePassword(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        pwd = BaseUserManager().make_random_password()
        myuser.set_password(pwd)
        # user.profile.signup_confirmation = True
        myuser.save()
        # auth.login(request,myuser)
        # Welcome Email
        subject = "Password Changed"
        message = "Hello "+myuser.first_name+"!! \n "+ "your changed password is : "+pwd+"  \n Admin"
        from_email = settings.EMAIL_HOST
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        messages.success(request, "A changed password has been sent to your email!!")
        return render(request,'authentication/index.html')
    else:
        messages.success(request, "Password reset failed!!")
        return render(request,'authentication/index.html')

@login_required
def changeProfilePassword(request):
    username = request.user
    if request.method == 'POST':
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
            user.set_password(password)
            user.save()
        except:
            error = "The password was not changed"
            return render(request, 'change_profile_password.html', {'error':error})
        success = "The password was changed successfully"
        return render(request, 'change_profile_password.html', {'success':success})
    else:
        return render(request, 'change_profile_password.html')

def deleteAccount(request):
    if request.method == 'POST':
        old_username = User.objects.filter(username=request.user).first()
        old_username.delete()
        auth.logout(request)
        messages.success(request, 'You account has been successfully deleted')
        return render(request, 'authentication/login.html')
    
    return redirect(dashboard)

def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect(home)


    
# below are the four methods being used frmo the stripe api into the transactions app

class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - lets capture the payment later
            # [customer_email] - lets you prefill the email input in the form
            # For full details see https:#stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param

            # If we want to identify the user when using webhooks we can pass client_reference_id  to checkout
            # session constructor. We will then be able to fetch it and make changes to our Django models.
            #
            # If we offer a SaaS service it would also be good to allow only authenticated users to purchase
            # anything on our site.

            checkout_session = stripe.checkout.Session.create(
                # client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'T-shirt',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '2000',
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


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

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
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)
