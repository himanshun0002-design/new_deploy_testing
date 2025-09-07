from django.contrib import admin
from .models import Society, Flat, ResidentProfile

@admin.register(Society)
class SocietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at')
    search_fields = ('name', 'address')
    ordering = ('name',)

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('society', 'flat_number', 'floor', 'is_occupied')
    list_filter = ('society', 'floor', 'is_occupied')
    search_fields = ('flat_number',)
    ordering = ('society', 'flat_number')

@admin.register(ResidentProfile)
class ResidentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'phone_number', 'is_owner', 'move_in_date')
    list_filter = ('is_owner', 'move_in_date')
    search_fields = ('user__username', 'phone_number')
    ordering = ('-move_in_date',)
