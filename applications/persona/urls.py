from django.contrib import admin
from django.urls import path
from rest_framework import routers


# Local
from .views import PersonaCRUD

router = routers.DefaultRouter()
router.register('api/persona', PersonaCRUD)
