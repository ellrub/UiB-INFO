from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100, default = 'Unknown')
    year_of_release = models.CharField(max_length = 4, default = 'Unknown')

    def __str__(self):
        return self.title