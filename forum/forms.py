from django import forms
from forum import models
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User


class BaseForumForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(BaseForumForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated():
            self.set_user(user)

    def set_user(self, user):
        self.instance.user = user
        self.fields['user_name'].initial = user.username
        self.fields['user_name'].widget.attrs['readonly'] = True

        self.fields['user_email'].initial = user.email
        self.fields['user_email'].widget.attrs['readonly'] = True

    class Meta:
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }


class ThreadForm(BaseForumForm):
    class Meta(BaseForumForm.Meta):
        labels = {
            'image': 'Upload image'
        }
        model = models.Thread
        fields = ['subject', 'user_name', 'user_email', 'message', 'image']


class PostForm(BaseForumForm):
    class Meta(BaseForumForm.Meta):
        model = models.Post
        fields = ['user_name', 'user_email', 'message']


class AuthenticationForm(auth_forms.AuthenticationForm):
    """
    Form for authorization by username and email
    """

    def __init__(self, request=None, *args, **kwargs):
        super(AuthenticationForm, self).__init__(request, *args, **kwargs)

        self.fields['username'].label = 'User name / Email'


class UserCreationForm(auth_forms.UserCreationForm):
    """
    Form that creates a user by username or email and
    password.
    """
    email = forms.EmailField(required=True)

    def clean_email(self):
        """
        Validate that the supplied email address is unique.
        """

        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("A user with that email already exists.")
        return self.cleaned_data['email']

    class Meta(auth_forms.UserCreationForm.Meta):
        fields = ["username", "email"]


class PostUpdateForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.fields['parent_post'].queryset = models.Post.objects.filter(thread=self.instance.thread)

    class Meta(BaseForumForm.Meta):
        model = models.Post
        fields = ['thread', 'message', 'parent_post']


class ThreadUpdateForm(forms.ModelForm):
    class Meta(BaseForumForm.Meta):
        model = models.Thread
        fields = ['sub_category', 'subject', 'message', 'image']