from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.cursos.views import CursosViewSet
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r'cursos', CursosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]
