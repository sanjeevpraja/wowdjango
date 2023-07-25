# accounts/urls.py
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import SignUp, MemberListView, MemberCreateView
from django.urls import path, include

app_name = 'members'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', csrf_exempt(SignUp.as_view()), name='signup'),
    path('list/', MemberListView.as_view(), name='member_list'),
    path('create/', MemberCreateView.as_view(), name='member_create'),
]