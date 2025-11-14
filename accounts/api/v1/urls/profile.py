from django.urls import path
from .. import views

urlpatterns = [
    # get profile model
    path('', views.ProfileAPIView.as_view(), name='user_profile'),
]

