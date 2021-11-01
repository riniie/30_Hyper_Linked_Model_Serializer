from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import StudentModelViewSet

router = DefaultRouter()
router.register('student', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest', include('rest_framework.urls')),
    path('', include(router.urls))
]
