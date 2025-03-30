from django.db import models
import uuid
from django.db.models import Q, CheckConstraint
from django.contrib.postgres.fields import ArrayField

# Create your models here.

# ORM

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


#Start incaria
class User(models.Model):

    user_id = models.UUIDField(primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique identifier for the patient")

    email = models.EmailField(blank=False,
        unique=True,
        null=False,
        help_text="Patient's email for login")

    name = models.CharField(max_length=200,
        null=False,
        blank=False,
        help_text="Patient's full name")

    GENDER_CHOICES = [
        ("Male", "male"),
        ("Female", "female"),
        ("Non-binary", "non-binary"),
        ("Other", "other"),
        ("Prefer not to say", "prefer not to say")
    ]

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        null=False,
        blank=False,
        help_text="Male, Female, Non-binary, Other, or Prefer not to say."
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        help_text="Patient's age"
    )

    health_conditions = ArrayField(
        base_field=models.CharField(max_length=100),
        null=True,
        blank=True,
        default=list,
        help_text="List of existing health conditions (e.g. 'Type 2 Diabetes', 'Hypertension')"
    )

    health_goals = ArrayField(
        base_field=models.CharField(max_length=100),
        null=True,
        blank=True,
        default=list,
        help_text="List of patient’s health goals (e.g. 'Lose weight', 'Improve sleep')"
    )

    motivators = ArrayField(
        base_field=models.CharField(max_length=100),
        null=True,
        blank=True,
        default=list,
        help_text="Key personal motivators for health (e.g. 'Family', 'Longevity')"
    )

    provider_code = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        help_text="Unique code linking the patient to a provider"
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        help_text="Date when user created the account."
    )

    active_status = models.BooleanField(
        default=True,
        help_text="Whether user is currently active."
    )

    # Add the age check constraint
    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(age__gte=0) & Q(age__lte=120),
                name="valid_age_range"
            )
        ]
# New model for chronic condition category table
class Category(models.Model):
    category_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique identifier for category"
    )
    category_name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        help_text="Name of the chronic condition category"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Brief description of the category"
    )

    def __str__(self):
        return self.category_name
    

#Condition table
class Condition(models.Model):
    condition_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique identifier for each chronic condition"
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        help_text="Name of the chronic condition"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Brief description of the condition"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text="Links the condition to a category"
    )
    common_symptoms = ArrayField(
        base_field=models.CharField(max_length=100),
        null=True,
        blank=True,
        help_text='List of common symptoms (e.g., ["Fatigue", "Fever"])'
    )

    def __str__(self):
        return self.name