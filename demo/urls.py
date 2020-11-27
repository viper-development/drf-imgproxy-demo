from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

app_name = 'demo'

router = DefaultRouter()
router.register('picture', views.PictureViewSet)

urlpatterns = [
    path('', include(router.urls))
]
