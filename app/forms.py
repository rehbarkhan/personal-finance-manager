from django import forms
from .models import Profile, Expense
from django.utils import timezone

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget = forms.DateInput(attrs={'type':'date'})
        self.fields['first_name'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['middle_name'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['last_name'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['email'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['contact'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['date_of_birth'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['address'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['city'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['state'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['country'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['zip_code'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = timezone.now()
        self.fields['transaction_type'].widget.attrs.update(
            {'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'}
        )
        self.fields['name'].widget.attrs.update({'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'})
        self.fields['sum'].widget.attrs.update({'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'})

        self.fields['date'].widget = forms.DateInput(
            attrs={
                'type':'date',
                'class':'w-full max-w-md px-5 py-2 border border-blue-400 ring-none focus:outline-none'
            }
        )