from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app1.views import *

router = DefaultRouter()
router.register('suv', SuvApiSet)
router.register('mijoz', MijozApiSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buyurtma/', BuyurtmaApi.as_view()),
    path('adminlar/', AdminApi.as_view()),
    path('aadmin/<int:pk>/', AdminApiOne.as_view()),
    path('haydovchilar/', HaydovchiApi.as_view()),
    path('haydovchi/<int:pk>/', HaydovchiApiOne.as_view()),
    path('', include(router.urls))
]
