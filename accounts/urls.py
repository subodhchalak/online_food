from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register_user/', views.register_user, name='register_user')
]