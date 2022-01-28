from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drinks.api_views import get_router_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(get_router_urls())),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenObtainPairView.as_view(), name='token_refresh'),
]
