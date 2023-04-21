from rest_framework.routers import DefaultRouter
from django.urls import path, include
from friends.api.view import FriendViewSet

app_name = 'friends'
router_friend = DefaultRouter()

router_friend.register('friend', FriendViewSet, basename='friend')