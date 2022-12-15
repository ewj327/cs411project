from django.shortcuts import render
from allauth.account.views import SignupView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# Create your views here.
class AccountSignupView(SignupView):
    template_name = "users/custom_signup.html"

class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter

account_signup_view = AccountSignupView.as_view()