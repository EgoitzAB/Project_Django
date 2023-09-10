from django import forms
from .models import Producto
from allauth.account.forms import LoginForm

class ProductoModelForm(forms.ModelForm):
    #name = forms.CharField(widget=forms.TextInput(attrs={'class':'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    #description = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    #slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-r'}), required=True)
    #precio = forms.CharField(
        #widget=forms.TextInput(
            #attrs={
             #   'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'
             #   }), 
            #required=True
              #  )
    
    class Meta:
        model=Producto
        fields= "__all__"

    def clean_price(self, *args, **kwargs):
        precio = self.cleaned_data.get("Producto__precio")
        precio = int(precio)
        if precio > 99:
            return precio
        else:
            raise forms.ValidationError("Price must be equal or higher than $1 == 100")
        
