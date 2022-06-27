from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField("이름", max_length=50)
    description = models.TextField("설명")
    
    class Meta:
        db_table = '카테고리'

    def __str__(self):
        return self.name
    
class Article(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    contents = models.TextField("본문")
    start_date = models.DateField("노출 시작일", auto_now_add=True) 
    end_date = models.DateField("노출 종료일", null=True, blank=True)
    
    class Meta:
        db_table = '아티클'
    
    def __str__(self):
        return f"{self.title} / {self.user.username} / " + str(self.start_date)
    


class Comment(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="작성자", on_delete=models.CASCADE)
    contents = models.TextField()
    
    class Meta:
        db_table = '댓글'
    
    def __str__(self):
        return f"{self.article.title} / {self.contents}"
    
    