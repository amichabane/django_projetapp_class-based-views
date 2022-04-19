from django.contrib import admin

# Register your models here.
from .models import Notes,NoteCategory

admin.site.register(Notes)
admin.site.register(NoteCategory)