from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    POST_STATUS_CHOICES = (("draft", "Draft"), ("published", "Published"))

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True, blank=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.CharField(
        max_length=10, choices=POST_STATUS_CHOICES, default="published"
    )
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return self.title
