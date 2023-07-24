
from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MyTokenObtainPairView


urlpatterns = [
    # path('Api_login/',views.obtain_auth_token)    
    # path('api_token/',TokenObtainPairView.as_view(),name='token_obtain_view'),
    path('Refresh_token/',TokenRefreshView.as_view(),name='Refresh_token'),
    path('custom_gettoken/',MyTokenObtainPairView.as_view(),name='gettoken'),
    
    
    
]