from django import forms
from complectations.models import Complectation
from phonenumber_field.formfields import PhoneNumberField


class ComplectationForm(forms.ModelForm):

    class Meta:
        model = Complectation
        fields = "__all__"
        exclude = ["date_create", "author", "balance", "procent", "slug"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Изменяем тип поля телефон на "tel"
        self.fields['phone'].widget.attrs.update({'class': 'block text-gray-700 text-sm font-bold mb-2', 'maxlength': '15'})