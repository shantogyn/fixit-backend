from django.contrib import admin
from django.urls import path, include
from FIXIT.views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('accounts.urls')),
    path('accounts/', include('accounts.urls')),
    #login token generation
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #token refresh
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path('service/', include('Service.urls')),


]
