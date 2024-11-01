from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

User = get_user_model()


class UserEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.NumberInput):
                field.widget = forms.TextInput(attrs=
                    {
                        'type': 'text',
                        'class': 'formatted-input'
                    }
                )

    class Meta:
        model = User
        fields = ['role', 'bonus', 'email', 'first_name', 'last_name', 'phone']


class UserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.NumberInput):
                field.widget = forms.TextInput(attrs=
                    {
                        'type': 'text',
                        'class': 'formatted-input'
                    }
                )

    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("bonus", "email", "phone", "first_name", "last_name", "role", "is_staff")