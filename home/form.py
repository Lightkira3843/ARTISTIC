

from django import forms
from .models import Product
from django.contrib.admin.widgets import AdminDateWidget

class ImageForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ("product_name", "artby", "price", "product_desc", "image")
