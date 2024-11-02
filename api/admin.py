from django.contrib import admin
from api.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','firstname','lastname' ,'money','turns']

admin.site.register(User, UserAdmin)
