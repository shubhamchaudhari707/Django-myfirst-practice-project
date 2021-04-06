from django.contrib import admin
from .models import Crudproject
# # Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id','first_name' ,'last_name' ,'email', 'username', 'password1']
#
#
class CrudAdmin(admin.ModelAdmin):
    list_display = ['id','name','subject','marks', 'user']
admin.site.register(Crudproject,CrudAdmin)