from product.models import Product as ProductModel
from product.models import Review as ReviewModel
from datetime import datetime
from rest_framework import serializers
from django.db.models import Avg


   
class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(read_only=True, slug_field='name')
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = ReviewModel
        fields = "__all__"
        # fileds = ["user", "content", "registered_date", "rating"] 
        
 
        
class ProductSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    
    review = serializers.SerializerMethodField()
    def get_review(self, obj):
        reviews = obj.review_set
        return {
            "최근 리뷰":ReviewSerializer(reviews.last()).data,
            "평균 평점":reviews.aggregate(Avg("rating"))
        }
        

    def validate(self, data):
        end_date = data.get("end_date", "")
        if end_date and end_date < datetime.now().date():
            raise serializers.ValidationError(
                detail={"error":"유효하지 않은 노출 종료 날짜입니다."},
            )
        return data
    
    
    def create(self, validated_data):
        product = ProductModel(**validated_data)
        product.save()
        product.dec += f"\n\n {product.registered_date.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다"
        product.save()
        return product
    
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "dec":
                value += f"\n\n {instance.registered_date.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다"
            setattr(instance, key, value)
        instance.save()
        instance.dec = f" {instance.updated_date.replace(microsecond=0, tzinfo=None)}에 수정되었습니다.\n\n"+instance.dec

        instance.save()
        return instance
    

    class Meta:
        model = ProductModel
        fields = "__all__"
        # fields = ["user", "name", "image", "dec", "registered_date", 
        #           "updated_date", "end_date", "is_active", "price", "review"]
    

        
        
            
        
    ## tiffitkftifkfcnrkc,