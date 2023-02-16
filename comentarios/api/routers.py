from rest_framework.routers import DefaultRouter

from comentarios.api.viewset import ComentVieeSet

router_coment = DefaultRouter()

router_coment.register(prefix='coment', viewset=ComentVieeSet, basename='coment')
