from django.db import models

class Category(models.Model):
    topic = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    author_avatar = models.CharField(max_length=1000)

    def __str__(self):
        return self.topic +' - ' + self.author

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #file_type = models.CharField(max_length=100)
    article_title = models.CharField(max_length=1000)