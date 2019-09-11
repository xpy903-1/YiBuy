from django.forms import ModelForm
from .models import PictureModel

class PictureForm(ModelForm):
    class Meta:
        model = PictureModel
        fields = '__all__'