# accounts/urls.py
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import SignUp
from django.urls import path, include

app_name = 'members'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', csrf_exempt(SignUp.as_view()), name='signup'),
]