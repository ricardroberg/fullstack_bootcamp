from django import forms
from .models import User
from django.forms import ModelForm


class SignIn(ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        # verify_email = forms.EmailField(label='Enter your email again', required=True)

        # def clean(self):
        #     """# GET ALL DATA FROM FORM, DICT FORMAT:
        #      {'name': 'Jhon Doe', 'email': 'jdoe@gmail.com',
        #      'verify_email': 'jdoe@gmail.com', 'text': 'test test test'}"""
        #
        #     all_clean_data = super().clean()
        #     email = all_clean_data['email']
        #     vmail = all_clean_data['verify_email']
        #
        #     if email != vmail:
        #         raise forms.ValidationError("MAKE SURE EMAILS MATCH!")


# class FormName(forms.Form):
#     name = forms.CharField()  # validators=[check_for_z] CUSTOM VALIDATION FUNCTION
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again', required=True)
#     text = forms.CharField(widget=forms.Textarea)

