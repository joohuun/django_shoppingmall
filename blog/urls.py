from django.urls import path, include
from . import views 


# 뷰셋
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('article',views.ArticleViewSet)


urlpatterns = [
    path('article/', views.ArticleView.as_view()),
    path('article/<art_id>', views.ArticleView.as_view()),
    # path('',include(router.urls)), # 뷰셋
]
