from django.contrib import admin
from .models import User
from .models import Goal
# Register your models here.
admin.site.register(User)
admin.site.register(Goal)
