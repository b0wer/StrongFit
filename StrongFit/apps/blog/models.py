from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    

    image_pub = models.ImageField(upload_to = 'posts/image', blank=True, )


    def __str__(self):
        return '{}'.format(self.title)


