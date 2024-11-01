from django import forms
from complectations.models import GroupProduct


class GroupForm(forms.ModelForm):

    class Meta:
        model = GroupProduct
        fields = "__all__"
        exclude = ["slug"]