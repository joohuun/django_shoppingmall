from django.db import models

# Create your models here.


class Product(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    name = models.CharField("상품명", max_length=50)
    image = models.FileField("썸네일", upload_to='productimg', null=True, blank=True)
    dec = models.TextField("상품설명")
    registered_date = models.DateTimeField("등록일", auto_now_add=True)
    updated_date = models.DateTimeField("수정시간", auto_now=True)
    end_date = models.DateField("노출 종료일", null=True, blank=True)
    is_active = models.BooleanField("활성화 여부")
    price = models.IntegerField("가격")
    
    class Meta:
        db_table = '상품'
    
    def __str__(self):
        return f"{self.name} / {self.price}"
    
    
class Review(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.SET_NULL, null=True)
    content = models.TextField("내용")
    registered_date = models.DateTimeField("등록일", auto_now_add=True)
    rating = models.IntegerField("평점")
    
    class Meta:
        db_table = '리뷰'
        
    def __str__(self):
        return f"{self.product} / {self.content}"
    
    

