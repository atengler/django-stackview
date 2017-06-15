from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from .models import Stack

User = get_user_model()


class BootstrapFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(BootstrapFormMixin, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class StackCreateForm(BootstrapFormMixin, forms.Form):
    name = forms.CharField(required=True, label=_('Name'))
    backend = forms.ChoiceField(choices=Stack.BACKEND_CHOICES, required=True, label='Backend')

    def clean(self):
        cleaned_data = super(StackCreateForm, self).clean()
        #TODO: call Jenkins here
        return cleaned_data

    def save_stack(self, author):
        name = self.cleaned_data.get('name', None)
        backend = self.cleaned_data.get('backend', None)
        if isinstance(author, User) and name and backend:
            Stack.objects.create(name=name, backend=backend, author=author)


class UserUpdateForm(BootstrapFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    pass
