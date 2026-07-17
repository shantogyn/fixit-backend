from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from FIXIT.views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('accounts.urls')),
    path('ac/', include('accounts.urls')),
    #login token generation
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #token refresh
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path('ser/', include('Service.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
