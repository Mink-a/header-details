from django.db import models

# Create your models here.
class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

class Relationship(models.Model):
  name = models.CharField(max_length=60)
  relationship = models.CharField(max_length=30)
  person = models.ForeignKey(Person, on_delete=models.PROTECT)

