from django import forms
from forum import models
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
            self.fields['user_name'].user_name = self._get_user_name(instance)
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
            return self._get_user_name(instance)
        else:
            return self.cleaned_data['user_name']

    def _get_user_name(self, instance):
        return "{0}, {1}".format(instance.user.last_name, instance.user.first_name)

