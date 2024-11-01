from django import forms

from complectations.models import Procurement


class ProcurementForm(forms.ModelForm):
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
        model = Procurement
        fields = "__all__"
        widgets = {
            "date_create": forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'style': ' width: 12rem !important;'
                }
            ),
        }
        exclude = ["author", "complectation", "price_procent"]