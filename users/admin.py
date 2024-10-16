from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'first_name', 'user_name')
    list_filter = ('email', 'first_name', 'user_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'created_at', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'user_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Personal Info', {'fields': ('first_name', 'about')}),
    )

    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff'),
        }), # The corrected code includes a comma after the closing parenthesis of the add_fieldsets tuple, ensuring proper tuple formatting.
    )

admin.site.register(NewUser, UserAdminConfig)






