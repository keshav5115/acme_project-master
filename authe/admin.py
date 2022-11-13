from django.contrib import admin

from authe.models import User


class useradmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'Department', 'role']


admin.site.register(User, useradmin)
