from django import forms

class PersonForm(forms.Form):
  first_name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'First Name',
      'class': 'form-control'
      }))
  last_name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Last Name',
      'class': 'form-control'
      }))

  father_name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Last Name',
      'class': 'form-control'
      }))

  age = forms.IntegerField(widget=forms.NumberInput(attrs={
      'placeholder': 'Age',
      'class': 'form-control'
      }), required=False)

class RelationshipForm(forms.Form):
  member_id = forms.CharField(widget=forms.HiddenInput, required=False)
  name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Name',
      'class': 'form-control col-6'
      }))
  relationship = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Relationship',
      'class': 'form-control col-6'
      }))
  age = forms.IntegerField(widget=forms.NumberInput(attrs={
      'placeholder': 'Age',
      'class': 'form-control col-6'
      }), required=False)
  del_flag = forms.BooleanField(initial=False, required=False)