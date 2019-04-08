from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField()
    blog_body = models.TextField()

