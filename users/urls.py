from django.urls import path

from users.api.api import ChangePasswordView
from users.views import GetMe

urlpatterns = [
    path('getme/', GetMe.as_view()),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]
