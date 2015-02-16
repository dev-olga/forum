from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=1024)
    auth_only = models.BooleanField(default=False)


class SubCategory(models.Model):
    name = models.CharField(max_length=1024)
    category = models.ForeignKey(Category)


class Thread(models.Model):
    sub_category = models.ForeignKey(SubCategory)
    subject = models.CharField(max_length=1024)
    message = models.CharField(max_length=1024)
    date = models.DateTimeField()
    user = models.ForeignKey('auth.User', default=None)
    user_name = models.CharField(max_length=1024, default=None)
    user_email = models.CharField(max_length=1024, default=None)


class Post(models.Model):
    thread = models.ForeignKey(Thread)
    subject = models.CharField(max_length=1024)
    message = models.CharField(max_length=1024)
    date = models.DateTimeField()
    user = models.ForeignKey('auth.User', default=None)
    user_name = models.CharField(max_length=1024, default=None)
    user_email = models.CharField(max_length=1024, default=None)
    parent_post = models.ForeignKey('self', default=None)