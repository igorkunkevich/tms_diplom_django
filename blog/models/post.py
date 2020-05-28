from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"pk": self.pk})

    def __str__(self):
        return f'"{self.title}" by {self.user.username}'
