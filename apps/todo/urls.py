from django.urls import path

from rest_framework import routers

from . import views

from .views import TaskViewSet


router = routers.DefaultRouter()

router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = []

urlpatterns += router.urls
