from django.contrib import admin
from .models import Project
from .models import ContactMessage
# Register your models here.

admin.site.register(Project)
admin.site.register(ContactMessage)