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

class RelationshipForm(forms.Form):
  member_id = forms.CharField(widget=forms.HiddenInput, required=False)
  name = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Name',
      'class': 'form-control'
      }))
  relationship = forms.CharField(widget=forms.TextInput(
    attrs={
      'placeholder': 'Relationship',
      'class': 'form-control'
      }))
  del_flag = forms.BooleanField(initial=False, required=False)
