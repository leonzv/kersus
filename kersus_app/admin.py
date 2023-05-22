from django.contrib import admin
from .models import Category, Participant

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user', 'profile_pic', 'created_at')
    list_filter = ('name', 'user', 'created_at')
    search_fields = ('name', 'description', 'user')
    ordering = ('name', 'user', 'created_at')
    filter_horizontal = ()
    fieldsets = ()

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_pic', 'category')
    list_filter = ('name', 'category')
    search_fields = ('name', 'category')
    ordering = ('name', 'category')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Participant, ParticipantAdmin)
