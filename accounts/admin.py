from atexit import register
from django.contrib import admin
from accounts.models import User, UserProfile


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active')
    list_filter = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active')
    readonly_fields = ('password', )
    ordering = ('-id', )
    
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pin_code', 'city', 'state', 'country')
    list_filter = ('id', 'pin_code', 'city', 'state', 'country')