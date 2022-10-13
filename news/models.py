from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

#
article = 'AR'
news = 'NW'
PostPositions = [(article, 'Статья'), (news, 'Новость')]


# Create your models here.

class Author(models.Model):
    authorname = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    rating = models.SmallIntegerField(default=0)

    #
    def update_rating(self):
        # post_rating = self.post_set_aggregate(postrating=Sum('rating'))
        post_rating = self.post_set_aggregate(postrating=Sum('rating'))
        p_rat = 0
        p_rat += post_rating.get('postrating')

        comment_rating = self.authorname.Comment_set_aggregate(commentrating=Sum('rating'))
        c_rat = 0
        c_rat += comment_rating.get('commentrating')

        self.rating = p_rat*3 + c_rat
        self.save()
        # pass

    #
    def some_method(self):
        #     pass
        self.Author = self.full_name.split()[0]


#

class Category(models.Model):
    context = models.TextField(unique=True, blank=True)
    # pass

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    post_datetime = models.DateTimeField(auto_now_add=True)
    typePost = models.CharField(max_length=2, choices=PostPositions, default=news)
    headPost = models.CharField(max_length=255, blank=True)
    textPost = models.TextField(blank=True)
    rating = models.SmallIntegerField(default=0)

    # pass
    def like(self):
        self.rating += 1
        self.save()

    #
    def dislike(self):
        if self.rating > 0:
            self.rating -= 1
            self.save()

    def preview(self):
        return self.textPost[:123] + '...'


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # pass


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    dateComment = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    #
    def like(self):
        self.rating += 1
        self.save()

    #
    def dislike(self):
        if self.rating > 0:
            self.rating -= 1
            self.save()
