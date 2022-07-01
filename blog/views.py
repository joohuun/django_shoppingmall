from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel
from blog.models import Category as CategoryModel
from blog.serializers import ArticleSerializer, CommentSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = ArticleModel.objects.filter(user=request.user) # 로그인된 사용자 게시물
        # articles = ArticleModel.objects.order_by("-start_date") # 전체 게시일 역순
        article_serializer = ArticleSerializer(articles, many=True).data
        return Response(article_serializer, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        request.data['user'] = request.user.id
        article_serializer = ArticleSerializer(data=request.data)
        
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(article_serializer.data, status=201)
        return Response(article_serializer.errors, status=400)
    
    
    def put(self, request, art_id):
        article = ArticleModel.objects.get(id=art_id)
        article_serializer = ArticleSerializer(article ,data=request.data, partial=True)
        # partial = True ==> 부분적로 수정가능하게 함
        
        if article_serializer.is_valid():
            article_serializer.save()
            return Response(article_serializer.data, status=200)
        
        return Response(article_serializer.errors, status=400)
    
    
    def delete(self, request, art_id):
        article = get_object_or_404(ArticleModel, id=art_id)
        article.delete()
        return Response({f"제목: {article.title} 삭제 되었습니다"})
    
    

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
            


    
# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = ArticleModel.objects.all()
#     serializer_class = ArticleSerializer 
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
        
        
        
        

        
    
    
        
        




    
        
    
