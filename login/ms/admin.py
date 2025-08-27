from django.contrib import admin
from .models import blog,custom_user
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(blog)

@admin.register(custom_user)
class custom_user_admin(UserAdmin):
    pass