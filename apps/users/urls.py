from django.urls import path
from .views.jwt import EmailTokenObtainPairView
from .views.register import RegisterView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("login/", EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", RegisterView.as_view(), name="register_user"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
