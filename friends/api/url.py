from rest_framework.routers import DefaultRouter

from friends.api.view import FriendViewSet

router_friend = DefaultRouter()

router_friend.register(prefix='friend', viewset=FriendViewSet, basename='friend')
