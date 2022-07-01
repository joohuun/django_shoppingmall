from django import views
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from rest_framework.views import APIView
from datetime import datetime
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from product import serializers
from product.models import Product as ProductModel
from product.models import Review as ReviewModel
from product.serializers import ProductSerializer, ReviewSerializer


# Create your views here.
class ProductView(APIView):
    def get(self, request):
        today = datetime.now()
        products = ProductModel.objects.filter(Q(end_date__gte=today, is_active=True) |
                                               Q(user=request.user))
        # products = ProductModel.objects.all()
        product_serailzer = ProductSerializer(products, many=True).data
        return Response(product_serailzer, status=status.HTTP_200_OK)
    

    def post(self, request):
        request.data['user'] = request.user.id
        product_serializer = ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
         
        return Response(product_serializer.errors, 
                        status=status.HTTP_400_BAD_REQUEST,
                        template_name='user_detail.html'
                        )
    
    
    def put(self, request, pro_id):
        product = ProductModel.objects.get(id=pro_id)
        product_serializer = ProductSerializer(product ,data=request.data, partial=True)
        # partial = True ==> 부분적으로 수정가능하게 함
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pro_id):
        product = get_object_or_404(ProductModel, id=pro_id)
        product.delete()
        return Response({f"상품: {product.name} 삭제 되었습니다."})

    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        return Response({"리뷰 작성 완료"})
