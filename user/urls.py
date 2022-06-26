from django import urls
from django.urls import path, include
from . import views



urlpatterns = [
    path('login/', views.UserAPIView.as_view()),
    path('logout/', views.UserAPIView.as_view()),
    
    path('', views.UserView.as_view()),
    path('<user_id>', views.UserView.as_view()),  # 회원정보 put, delete
]
