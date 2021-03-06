from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from lcb import views


router = routers.DefaultRouter()
router.register('boards', views.BoardViewSet)
router.register('lanes', views.LaneViewSet)
router.register('cards', views.CardViewSet)

api_patterns = [
    path('login/', views.LoginView.as_view()),
    path('version/', views.VersionView.as_view()),
    path('', include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
]
