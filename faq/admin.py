from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django.db import models

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }