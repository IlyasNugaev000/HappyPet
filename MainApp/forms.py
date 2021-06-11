from django.forms import ModelForm
from .models import Owner

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'app-form-control',
                'placeholder': self.Meta.model._meta.get_field(field).verbose_name.title()
            })