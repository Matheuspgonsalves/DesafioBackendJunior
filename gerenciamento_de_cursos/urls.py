from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.cursos.views import CursosViewSet

router = DefaultRouter()
router.register(r'cursos', CursosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
