from django.urls import path
from .views import RegisterationView
from rest_framework_simplejwt.views import(TokenObtainPairView,
TokenRefreshView)


app_name = "Users"

urlpatterns = [
    path('register/', RegisterationView.as_view(),
    name="registeration"),
    path('token/', TokenObtainPairView.as_view(),
    name="get-token"),
    path('token/refresh/', TokenRefreshView.as_view(),
    name="refresh-token"),
]