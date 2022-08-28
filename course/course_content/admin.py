import imp
from django.contrib import admin
from.models import Course, Lesson, Tag

# Register your models here.

admin.site.register(Tag)
admin.site.register(Lesson)
admin.site.register(Course)
