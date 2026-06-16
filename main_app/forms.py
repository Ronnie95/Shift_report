from django import forms
from .models import Shift

class ShiftReport(forms.ModelForm):
    class Meta:
        model = Shift
        fields = [
            'date',
            'shift_name',
            'people_amount',
            'breakdowns',
            'assistance_needed',
            'additiional_comments'
        ]

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'breakdowns': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe any breakdowns...'
            }),
            'additiional_comments': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Additional notes for next shift...'
            }),
        }