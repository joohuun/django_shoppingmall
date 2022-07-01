from django.urls import path, include
from . import views
from product.views import ReviewViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('review', ReviewViewSet, basename='review') # 리뷰


urlpatterns = [
    # path('', include(router.urls)),
    path('', views.ProductView.as_view()),  
    path('<pro_id>', views.ProductView.as_view()),
    path('', include(router.urls)),
]