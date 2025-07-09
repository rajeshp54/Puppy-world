from django.db import models
from django.contrib.auth.models import User

class Puppy(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # user who added it

    age_year = models.IntegerField()
    age_month = models.IntegerField()
    breed = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    
    has_kci_certificate = models.BooleanField(default=False)
    kci_certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)

    PURPOSE_CHOICES = [
        ('buy', 'Buy'),
        ('sale', 'Sale'),
        ('matting', 'Matting'),
    ]
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES, default='buy')

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # ✅ New field

    image = models.ImageField(upload_to='puppy_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.breed} by {self.owner.username}"

    def age_display(self):
        return f"{self.age_year} year(s), {self.age_month} month(s)"
