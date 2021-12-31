from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


# each blog post is going to connect to a model in out database
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   # direct linking an author to an authorization user; i.e. the super user is basically someone who can author new posts
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)   # blank=True bcoz maybe you dont want to publish it yet and null = True bcoz maybe you dont have any publication date, basically published_date can be blank and null


    # method to set up the publication date i.e. published_date
    # whenever we click the publish button the time will set to the current time
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # CBV looks for get_absolute_url method to redirect the user
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    # we will have the list of comments and some of them will be approved comments and some will be non approved comments
    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name = 'comments', on_delete=models.CASCADE)   # connecting each comment to an actual post
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)  # same as published_date

    def approve(self):
        self.approved_comment = True
        self.save()

    # CBV looks for get_absolute_url method to redirect the user
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text