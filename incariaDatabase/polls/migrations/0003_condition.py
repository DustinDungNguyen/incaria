# Generated by Django 5.1.6 on 2025-03-30 10:04

import django.contrib.postgres.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('condition_id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier for each chronic condition', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the chronic condition', max_length=255, unique=True)),
                ('description', models.TextField(blank=True, help_text='Brief description of the condition', null=True)),
                ('common_symptoms', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, help_text='List of common symptoms (e.g., ["Fatigue", "Fever"])', null=True, size=None)),
                ('category', models.ForeignKey(help_text='Links the condition to a category', on_delete=django.db.models.deletion.CASCADE, to='polls.category')),
            ],
        ),
    ]
