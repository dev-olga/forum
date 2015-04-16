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

    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.user:
            self.fields['user_name'].user_name = instance.user.get_full_name()
            self.fields['user_name'].widget.attrs['readonly'] = True

            self.fields['user_email'] = instance.user.email
            self.fields['user_email'].widget.attrs['readonly'] = True

    def save(self, *args, **kwargs):
        self.instance.date = datetime.datetime.now()
        super(ThreadForm, self).save(*args, **kwargs)

    def clean_user_email(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.user:
            return instance.user.email
        else:
            return self.cleaned_data['user_email']

    def clean_user_name(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.user:
            return instance.user.get_full_name()
        else:
            return self.cleaned_data['user_name']


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

    email = forms.EmailField()
