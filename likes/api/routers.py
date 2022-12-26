from rest_framework.routers import DefaultRouter

from likes.api.viewset import LikesViewSet

router_likes = DefaultRouter()

router_likes.register(prefix='likes', viewset=LikesViewSet, basename='likes')
