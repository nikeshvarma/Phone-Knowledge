from django import forms
from USER.models import Profile, Review, QuestionAnswers


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'name', 'phone_number', 'address', 'profile_picture']

        widgets = {
            'user': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']

        widgets = {
            'review': forms.TextInput(attrs={'class': 'form-control'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswers
        fields = ['question']

        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
        }
