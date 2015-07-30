from django.contrib import admin
from .models import Entry
from .actions import make_published, export_as_excel

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

	list_display = ('id', 'title', 'published', 'image', 'get_url_image', 'created')
	actions = (make_published, export_as_excel)

	def get_url_image(self, entry):
		url = entry.url_image()
		tag = "<img src='%s' width='100px' >" % url
		return tag
	get_url_image.allow_tags = True