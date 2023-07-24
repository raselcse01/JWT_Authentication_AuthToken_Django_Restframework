from django.contrib import admin
from django.urls import path, include
from app2 import views
from rest_framework.routers import DefaultRouter

#Creating Router objects
router = DefaultRouter()

#Register StudentViewSet with Router
router.register('studentapi/', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]
