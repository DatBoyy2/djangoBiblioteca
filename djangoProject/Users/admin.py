from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email','name','surname','usertype','created_at','img','is_active')
    list_filter = ('usertype',)
    fieldsets = (
        (None,{'fields':('email','usertype', 'img', 'name', 'surname', 'password')}),
        ('Permisions',{'fields':( 'is_active','is_staff')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':( 'email', 'usertype', 'img', 'name', 'surname','password1','password2','is_active','is_staff')
        }),
    )
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
