from django.contrib import admin
from SeedMgmt.models import *
from django import forms
from datetime import datetime


class TagAdmin(admin.ModelAdmin):
	list_filter = ['deleted']
	search_fields = ['tag_type','tag_value']

	list_display = ['tag_type','tag_value','deleted','created_by','updated_by']

	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return True

	def has_change_permission(self, request, obj=None):
		return True

	def has_add_permission(self, request, obj=None):
		return True

admin.site.register(Tag,TagAdmin)


class SeedAdmin(admin.ModelAdmin):
	list_filter = ['status']

	list_display = ['row','column','status','tag']

	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return True

	def has_change_permission(self, request, obj=None):
		return True

	def has_add_permission(self, request, obj=None):
		return True

admin.site.register(Seed,SeedAdmin)