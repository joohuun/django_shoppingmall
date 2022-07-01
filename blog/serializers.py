import re
from rest_framework import serializers
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel
from blog.models import Category as CategoryModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name"]
        

class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField()    
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = CommentModel
        fields = "__all__"
        

class ArticleSerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)
    """
    아티클모델은 코멘트객체를 상속하지 않으므로
    _set을 사용, 역참조하여 가저온다
    """     
    
    category = serializers.SerializerMethodField()
    def get_category(self, obj): 
        # return obj.category.name
        return [category.name for category in obj.category.all()] 
    """
    아티클모델은 카테고리를 FK로 상속 하고 있음, 위의 obj는 article임
    매니투매니관계는 반복문을 사용하여 article의 category.name를 가져옴
    """
    
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    # user = serializers.SerializerMethodField()    
    # def get_user(self, obj):
    #     # print(obj.user.username)
    #     return obj.user.username
    """
    아티클모델은 유저를 FK로 상속하고 있음, 위의 obj는 article임
    원투매니관계는 반복문 사용안하고 이름으로 가져올 수 있음
    """     
    
    class Meta:
        model = ArticleModel
        fields = "__all__"