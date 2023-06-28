from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'exercise'

urlpatterns = [
    # path('login-success/', views.login_success, name='login-success'),
    path('', views.ExerciseView.as_view(), name='exercise'),
    path('list/', views.ExerciseListView.as_view(), name='exercise_list'),
    path('create/', views.ExerciseCreateView.as_view(), name='exercise_create'),
    path('delete/<int:pk>/', views.ExerciseDeleteView.as_view(), name='exercise_delete'),
    path('detail/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('edit/<int:pk>/', views.exercise_edit, name='exercise_edit'),
    path('sorry/', views.sorry, name='sorry'),
]
