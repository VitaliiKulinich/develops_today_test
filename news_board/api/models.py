from django.db import models


class Post(models.Model):
    """Model for posts"""

    title = models.CharField(max_length=128)
    link = models.CharField(max_length=128, unique=True)
    creation_date = models.DateTimeField(editable=False, auto_now=True)
    amount_of_upvotes = models.IntegerField(editable=False, default=0)
    author_name = models.CharField(max_length=64)

    def upvote(self):
        """Increment amount of upvotes for current post"""

        self.amount_of_upvotes += 1
        self.save(force_update=True)

    class Meta:
        ordering = ["creation_date"]


class Comment(models.Model):
    """Model for comments of posts"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=64)
    content = models.TextField()
    creation_date = models.DateTimeField(editable=False, auto_now=True)
