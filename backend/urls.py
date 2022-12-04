from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import status
from location import views

router = routers.DefaultRouter()
router.register(r'locs', views.LocView, 'locs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/get_user_location/', views.UserLoc.as_view()),
path('api/generate_location/', views.GenerateLoc.as_view()),
]