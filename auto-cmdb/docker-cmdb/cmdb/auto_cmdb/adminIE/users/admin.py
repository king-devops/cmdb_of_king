# Register your models here.

# admin.py
from django.contrib import admin
from users.models import UsersProfile

class UsersProfileAdmin(admin.ModelAdmin):  
    pass

# 注册
admin.site.register(UsersProfile, UsersProfileAdmin)
