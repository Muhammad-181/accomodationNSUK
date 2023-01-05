from django import forms

from .models import Property, Image


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = (
            'instituition', 'title', 'bathroom', 
            'bedroom', 'building_size_in_SQFT', 
            'description', 'price', 'thumbnail',
            
        ) 

        widgets = {
            'instituition': forms.Select(attrs={
                'class': 'form-select border-black py-3'
            }),
            'bedroom': forms.Select(attrs={
                'class': 'form-select border-black py-3'
            }),
            'bathroom': forms.Select(attrs={
                'class': 'form-select border-black py-3'
            }),
            'title': forms.TextInput(attrs={
                'class': 'input-group mb-3 py-3 form-control'
            }),
            'building_size_in_SQFT': forms.TextInput(attrs={
                'class': 'input-group mb-3 form-control'
            }),
            'price': forms.TextInput(attrs={
                'class': 'input-group mb-3 form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'input-group mb-3 py-3 form-control'
            }),
           
        }




class ImageForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.FileInput(attrs={"multiple":True}), required=False)
    class Meta:
        model = Image
        fields = ('images',)

  




# class PropertyForm(forms.ModelForm):
#     class Meta:
#         model = Property
#         fields = (
#             'instituition', 'title', 'bathroom', 
#             'bedroom', 'building_size_in_SQFT', 
#             'description', 'price', 'image',
            
#          )
#         widgets = {
#              'instituition': forms.Select(attrs={
#                 'class': 'form-select border-black py-3'
#             }),
#              'bedroom': forms.Select(attrs={
#                 'class': 'form-select border-black py-3'
#             }),
#              'bathroom': forms.Select(attrs={
#                 'class': 'form-select border-black py-3'
#             }),
#             'title': forms.TextInput(attrs={
#                 'class': 'input-group mb-3 py-3 form-control'
#             }),
#             'building_size_in_SQFT': forms.TextInput(attrs={
#                 'class': 'input-group mb-3 form-control'
#             }),
#             'price': forms.TextInput(attrs={
#                 'class': 'input-group mb-3 form-control'
#             }),
#             'description': forms.Textarea(attrs={
#                 'class': 'input-group mb-3 py-3 form-control'
#             }),
           
#         }