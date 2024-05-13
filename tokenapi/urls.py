from django.urls import path
from .views import CustomAuthToken  # 아래 경로와 같음
# from tokenapi.views import CustomAuthToken  # tokenapi 폴더의 views.py

urlpatterns = [
    path("api-token-auth/", CustomAuthToken.as_view()),
]