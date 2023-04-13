from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Review, Comment

admin.site.register(Review)
admin.site.register(Comment)