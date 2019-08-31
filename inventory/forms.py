from django import forms
from .models import Laptops,Desktops,Mobiles,predict

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = ('type', 'price', 'quantity', 'status')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktops
        fields = ('type', 'price', 'quantity', 'status')
        

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobiles
        fields = ('type', 'price', 'quantity', 'status')

class Predict(forms.ModelForm):
    class Meta:
        model = predict
        fields = ('type', 'date')