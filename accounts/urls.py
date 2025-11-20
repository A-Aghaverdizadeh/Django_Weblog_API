from django.urls import path, include
from .views import email

urlpatterns = [
    path("", include("rest_framework.urls")),
    # path('api/v1/', include('accounts.api.v1.urls')),
    path("api/v2/", include("djoser.urls")),
    path("email", email, name='email'),
]
