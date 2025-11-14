from django.urls import path
from .. import views

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    ## changepassword
    path('change-password/', views.PasswordRestAPIView.as_view(), name='change_password'),
    ## resetpassword

    # activate user
    path('activate-user/<str:token>', views.ActivateUserAPIView.as_view(), name='activate-user'),
    path('resend-activation-email/', views.ResendActivateUserAPIView.as_view(), name='resend-activate-email'),

    # token
    path('token-login/', views.CustomObtainAuthToken.as_view(), name="token-login"),
    path('token-logout/', views.CustomDiscartAuthToken.as_view(), name="token-logout"),
    # JWT

    # email sending
    path('test-email', views.TestAPIEmailSend.as_view(), name='test-email'),
]

