from rest_framework.routers import DefaultRouter

from posts.api.views import PostsViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='posts', viewset=PostsViewSet, basename='posts')
