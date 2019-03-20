from django import forms
class Insertform(forms.Form):
    productnumber=forms.IntegerField(
        label='enter product number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'productnumber'
            }
        )
    )
    productname = forms.CharField(
        label='enter product name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'productname'
            }
        )
    )
    productcost = forms.IntegerField(
        label='enter product cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'productcost'
            }
        )
    )
    productclass = forms.CharField(
        label='enter product class',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'productclass'
            }
        )
    )
    productweight = forms.IntegerField(
        label='enter product weight',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product weight'
            }
        )
    )
class Updateform(forms.Form):
    productnumber = forms.IntegerField(
        label='enter product number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'productnumber'
            }
        )
    )
    productcost = forms.IntegerField(
        label='enter product cost',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'productcost'
            }
        )
    )
class Deleteform(forms.Form):
    productnumber = forms.IntegerField(
        label='enter product number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'productnumber'
            }
        )
    )