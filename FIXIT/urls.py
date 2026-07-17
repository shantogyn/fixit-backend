from django.contrib import admin
from django.urls import path, include
from FIXIT.views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
        path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path('service/', include('Service.urls')),


]
