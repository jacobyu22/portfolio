from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField()
    blog_body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.blog_body[:100]

    def pub_date_short(self):
        return self.publish_date.strftime('%b %e %Y')
