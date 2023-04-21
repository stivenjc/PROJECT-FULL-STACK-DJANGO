from django.urls import path

from users.api.api import ChangePasswordView
from users.views import GetMe

app_name = 'users'

urlpatterns = [
    path('getme/', GetMe.as_view(), name='getme'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]
