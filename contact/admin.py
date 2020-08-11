from django.contrib import admin
from .models import Conatct
# Register your models here.

@admin.register(Conatct)
class AdminContact(admin.ModelAdmin):
    
    list_display = ['id', 'name', 'phone', 'email', 'contact_of']
