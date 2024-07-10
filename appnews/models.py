from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
