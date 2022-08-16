from django.contrib import admin

from .models import Tutorial, Teacher

# Register your models here.

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'published']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'professional', 'age']