from django.db import models
from django.conf import settings 
from django.contrib.auth.models import User

#검색 모델
class Search(models.Model):
    region = models.CharField(max_length=30)

#게시물 모델
class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  #객체가 추가될 때의 시간을 date에 넣을 수 있음
 
    def __str__(self): #게시글 제목
        return self.title

#게시물 댓글    
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment   