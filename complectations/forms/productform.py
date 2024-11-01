from django import forms
from complectations.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "date_order": forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'style': ' width: 12rem !important;'
                }
            ),
            "date_shipment": forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'style': ' width: 12rem !important;'
                }
            )
        }
        exclude = ["author", "complectation", "sum_price_count", "remains"]
