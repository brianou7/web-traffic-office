from django.forms import ModelForm

from .models import Owner


class OwnerForm(ModelForm):

    class Meta:
        model = Owner
        fields = ['type', 'identification_type', 'identification_number', 'username', 'password']
        exclude = ['user']
