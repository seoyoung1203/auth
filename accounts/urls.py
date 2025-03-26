from django.urls import path
from . import views #views.signup

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='singup'),
    path('login/', views.login, name='login'),
]
