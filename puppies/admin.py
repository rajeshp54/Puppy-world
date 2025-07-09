from django.contrib import admin
from .models import Puppy

@admin.register(Puppy)
class PuppyAdmin(admin.ModelAdmin):
    list_display = ['id', 'breed', 'age_year', 'age_month', 'owner']
