from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

from backend_red_social import settings
from comentarios.api.routers import router_coment
from likes.api.routers import router_likes
from posts.api.routers import router_posts
from users.api.api import LogoutView, RegisterAPI
from users.api.router import router_user

schema_view = get_schema_view(
    openapi.Info(
        title="RED SOCIAL DE ADRIAN",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jimenezcardenasad@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('register/users/', RegisterAPI.as_view(), name='register'),
                  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('logout/', LogoutView.as_view(), name='auth_logout'),
                  path('users/', include('users.urls')),
                  path('', include(router_user.urls)),
                  path('', include(router_coment.urls)),
                  path('', include(router_posts.urls)),
                  path('', include(router_likes.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
