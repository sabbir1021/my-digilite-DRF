from django.urls import path
from .views import ProfileView , UserCreate, UserUpdate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('user_create/', UserCreate.as_view(), name='user_create'),
    path('user/<int:pk>', UserUpdate.as_view(), name='user'),
]
