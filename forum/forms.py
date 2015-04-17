from django import forms
from forum import models
from django.contrib.auth import forms as auth_forms
import datetime


class ThreadForm(forms.ModelForm):
    class Meta:
        model = models.Thread
        fields = ['subject', 'user_name', 'user_email', 'message', 'image']
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 10})
        }
        labels = {
            'image': 'Upload file'
        }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }

    def __init__(self, user=None, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated():
            self.set_user(user)

    def save(self, *args, **kwargs):
        self.instance.date = datetime.datetime.now()
        super(ThreadForm, self).save(*args, **kwargs)
    #
    # def clean_user_email(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.user:
    #         return instance.user.email
    #     else:
    #         return self.cleaned_data['user_email']
    #
    # def clean_user_name(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.user:
    #         return instance.user.username
    #     else:
    #         return self.cleaned_data['user_name']

    def set_user(self, user):
        self.instance.user = user
        self.fields['user_name'].initial = user.username
        self.fields['user_name'].widget.attrs['readonly'] = True
        # self.fields['user_name'].widget.attrs['disabled'] = True

        self.fields['user_email'].initial = user.email
        self.fields['user_email'].widget.attrs['readonly'] = True
        # self.fields['user_email'].widget.attrs['disabled'] = True


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
