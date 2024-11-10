from django.contrib import admin
from .models import User, Trip, CompanionRequest


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'age', 'location', 'phone_number', 'created_at')
    search_fields = ('username', 'first_name', 'last_name', 'location')
    list_filter = ('created_at',)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_location', 'end_location', 'date', 'seats_available', 'created_at')
    search_fields = ('start_location', 'end_location', 'user__username')
    list_filter = ('date', 'created_at')
    date_hierarchy = 'date'


@admin.register(CompanionRequest)
class CompanionRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_location', 'end_location', 'date', 'created_at')
    search_fields = ('start_location', 'end_location', 'user__username')
    list_filter = ('date', 'created_at')
    date_hierarchy = 'date'
