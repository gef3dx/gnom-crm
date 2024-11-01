from django import forms
from complectations.models import Provider


class ProviderForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = "__all__"
