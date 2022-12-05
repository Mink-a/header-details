from django.forms import formset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render

from core.forms import PersonForm,RelationshipForm
from core.models import Person, Relationship

# Create your views here.
def index(request):
  people = Person.objects.all()
  return render(request, 'index.html', context={'people':people})

def person_profile(request):
  person_form = PersonForm()
  RelationshipFormSet = formset_factory(RelationshipForm, extra=3)
  formset = RelationshipFormSet()

  if request.method == 'POST':
    person_form = PersonForm(request.POST)
    if person_form.is_valid():
      person = Person.objects.create(
        first_name=person_form.cleaned_data['first_name'],
        last_name=person_form.cleaned_data['last_name'],
        father_name=person_form.cleaned_data['father_name'],
        age=person_form.cleaned_data['age'],
      )

      formset = RelationshipFormSet(request.POST)
      if formset.is_valid():
        for form in formset:
          if form.cleaned_data.get('name'):
            member=Relationship.objects.create(
              name=form.cleaned_data['name'],
              relationship=form.cleaned_data['relationship'],
              person=person,
              age=form.cleaned_data['age']
            )
          return redirect('home')
      
  else:
    person_form = PersonForm()
    formset = RelationshipFormSet()

    return render(request, 'profile.html', context={
      'formset':formset,
      'form':person_form
    })

def person_profile_update(request, person_id):
  person = Person.objects.get(pk=person_id)
  person_form = PersonForm()
  RelationshipFormSet = formset_factory(RelationshipForm, extra=1)
  formset = RelationshipFormSet()

  if request.method == 'POST':
    person_form = PersonForm(request.POST)
    if person_form.is_valid():
      person.first_name=person_form.cleaned_data['first_name']
      person.last_name=person_form.cleaned_data['last_name']
      person.father_name=person_form.cleaned_data['father_name']
      person.age=person_form.cleaned_data['age']
      person.save()

      formset = RelationshipFormSet(request.POST)
      if formset.is_valid():
        for form in formset:
          if form.cleaned_data.get('del_flag'):
            # Delete
            member = Relationship.objects.get(pk=form.cleaned_data['member_id'])
            member.delete()
            continue

          if form.cleaned_data.get('member_id'):
            # update
            member = Relationship.objects.get(pk=form.cleaned_data['member_id'])
            member.name = form.cleaned_data['name']
            member.relationship = form.cleaned_data['relationship']
            member.age = form.cleaned_data['age']
            member.save()
          else:
            # Add new
            if form.cleaned_data.get('name'):
              member=Relationship.objects.create(
                name=form.cleaned_data['name'],
                relationship=form.cleaned_data['relationship'],
                age=form.cleaned_data['age'],
                person=person
              )
      

  person_form = PersonForm(initial={
    'first_name':person.first_name,
    'last_name':person.last_name,
    'father_name':person.father_name,
    'age':person.age
  })

  members = Relationship.objects.filter(person_id=person.id)
  data = []
  for member in members:
    mem_dict = {
      'member_id':member.id,
      'name':member.name,
      'age': member.age,
      'relationship':member.relationship,
    }
    data.append(mem_dict)
  formset = RelationshipFormSet(initial=data)
  
  return render(request, 'update.html', context={
    'formset':formset,
    'form':person_form,
    'person':person
  })