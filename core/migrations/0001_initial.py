# Generated by Django 4.1.3 on 2022-12-03 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('relationship', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.person')),
            ],
        ),
    ]
