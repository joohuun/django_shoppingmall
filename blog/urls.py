from django.urls import path, include
from . import views 
from blog.views import CommentsViewSet

# 뷰셋
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('comment', CommentsViewSet, basename='comment') # (댓글)

# router.register('article',views.ArticleViewSet)

urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('<art_id>', views.ArticleView.as_view()),
    path('', include(router.urls)),    
    # path('',include(router.urls)), # 뷰셋
]
