from django.contrib import admin
from django.urls import path , include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
