from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=1024)
    auth_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=1024)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Thread(models.Model):
    sub_category = models.ForeignKey(SubCategory)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1024)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey('auth.User', default=None, null=True)
    user_name = models.CharField(max_length=100, default=None, null=True, blank=True)
    user_email = models.EmailField(max_length=100, default=None, null=True, blank=True)
    image = models.ImageField(upload_to='threads/', default=None, null=True, max_length=1024, blank=True)

    def __str__(self):
        return self.subject


class Post(models.Model):
    thread = models.ForeignKey(Thread)
    message = models.CharField(max_length=1024)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey('auth.User', default=None, null=True)
    user_name = models.CharField(max_length=100, default=None, null=True, blank=True)
    user_email = models.EmailField(max_length=100, default=None, null=True, blank=True)
    parent_post = models.ForeignKey('self', default=None, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', default=None, null=True, max_length=1024, blank=True)

    def __str__(self):
        return self.message