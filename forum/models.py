from django.db import models
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/forum/media/')


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
    user = models.ForeignKey('auth.User', default=None, null=True)
    user_name = models.CharField(max_length=1024, default=None, null=True)
    user_email = models.CharField(max_length=1024, default=None, null=True)
    image = models.ImageField(storage=fs, upload_to='threads', default=None, null=True, max_length=1024, blank=True)


class Post(models.Model):
    thread = models.ForeignKey(Thread)
    subject = models.CharField(max_length=1024)
    message = models.CharField(max_length=1024)
    date = models.DateTimeField()
    user = models.ForeignKey('auth.User', default=None, null=True)
    user_name = models.CharField(max_length=1024, default=None, null=True)
    user_email = models.CharField(max_length=1024, default=None, null=True)
    parent_post = models.ForeignKey('self', default=None, null=True)
    image = models.ImageField(storage=fs, upload_to='posts', default=None, null=True, max_length=1024)