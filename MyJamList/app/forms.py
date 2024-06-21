"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


from django import forms
from django.db import models
from .models import Songs


class SongForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ['title', 'rating', 'link', 'file']
        
class UpdateSongForm(forms.Form):
    title = forms.ModelChoiceField(queryset=Songs.objects.none(), empty_label="Select Song")
    rating = forms.ChoiceField(choices=[(i, str(i)) for i in range(0, 6)])

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UpdateSongForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['title'].queryset = Songs.objects.filter(user=user)