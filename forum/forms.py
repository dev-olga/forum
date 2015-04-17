from django import forms
from forum import models
from django.contrib.auth import forms as auth_forms
import datetime


class BaseForumForm(forms.ModelForm):
    class Meta:
        labels = {
            'image': 'Upload file'
        }
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 5})

        }

    def __init__(self, user, *args, **kwargs):
        super(BaseForumForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated():
            self.set_user(user)

    # def save(self, *args, **kwargs):
    #     self.instance.date = datetime.datetime.now()
    #     super(BaseForumForm, self).save(*args, **kwargs)

    def set_user(self, user):
        self.instance.user = user
        self.fields['user_name'].initial = user.username
        self.fields['user_name'].widget.attrs['readonly'] = True

        self.fields['user_email'].initial = user.email
        self.fields['user_email'].widget.attrs['readonly'] = True


class ThreadForm(BaseForumForm):
    class Meta(BaseForumForm.Meta):
        model = models.Thread
        fields = ['subject', 'user_name', 'user_email', 'message', 'image']


class PostForm(BaseForumForm):
    class Meta(BaseForumForm.Meta):
        model = models.Post
        fields = [ 'user_name', 'user_email', 'message', 'image']

    # def __init__(self, user, *args, **kwargs):
    #     super(PostForm, self).__init__(user, *args, **kwargs)

    # def __init__(self, user, parent_post, *args, **kwargs):
    #     super(PostForm, self).__init__(user, *args, **kwargs)
    #     self.instance.parent_post = parent_post


class AuthenticationForm(auth_forms.AuthenticationForm):
    """
    Form for authorization by username and email
    """

    def __init__(self, request=None, *args, **kwargs):
        super(AuthenticationForm, self).__init__(request, *args, **kwargs)

        self.fields['username'].label = 'User name / Email'


class UserCreationForm(auth_forms.UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    class Meta(auth_forms.UserCreationForm.Meta):
        fields = ("username", "email", "first_name", "last_name")

    email = forms.EmailField(required=True)
