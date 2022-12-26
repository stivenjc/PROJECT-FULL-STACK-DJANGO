from rest_framework.routers import DefaultRouter

from users.api.api import UserApipViewSet

router_user = DefaultRouter()

router_user.register(prefix='users', viewset=UserApipViewSet, basename='users')
