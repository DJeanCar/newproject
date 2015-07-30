from django.contrib import admin
from .models import Entry
from .actions import make_published, export_as_excel

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

	list_display = ('id', 'title', 'published')
	actions = (make_published, export_as_excel)