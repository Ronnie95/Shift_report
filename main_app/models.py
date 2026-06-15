from django.db import models

# Create your models here.

class Shift(models.Model):
    date = models.DateField()
    shifts = (
        ("Red Shift", "Red Shift"),
        ("Blue Shift", "Blue Shift"),
        ("Green Shift", "Green Shift"),
        ("Orange Shift", "Orange Shift"),
    )
    shift_name = models.CharField(max_length=30, choices=shifts)
    people_amount = models.IntegerField()
    breakdowns = models.CharField(max_length=500)
    assistance = (
        ("Yes", "Yes"),
        ("No", "No"),
    )
    assistance_needed = models.CharField(max_length=30, choices=assistance)
    additiional_comments = models.CharField(max_length=500)

    def __str__(self):
        return self.date
    
