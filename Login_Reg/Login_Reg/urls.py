
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# class base view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MyTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/loginapi/', obtain_auth_token),

    # class base view
    path('api/tokenapi/', MyTokenObtainPairView.as_view()),
    path('api/refreshapi/', TokenRefreshView.as_view()),
]
