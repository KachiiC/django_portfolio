from django.db import models


class MMANews(models.Model):
    article = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=250)
    img_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name