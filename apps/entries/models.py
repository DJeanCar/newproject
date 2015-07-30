from django.db import models

class TimeStampModel(models.Model):

	created = models.DateField(auto_now_add=True)
	update = models.DateField(auto_now=True)

	class Meta:
		abstract = True

class EntryQuerySet(models.QuerySet):

	def published(self):
		return self.filter(published = True)

	def not_published(self):
		return self.filter(published = False)


class Entry(TimeStampModel):

	title = models.CharField(max_length=50)
	content = models.TextField()
	published = models.BooleanField(default = False)
	image = models.ImageField(upload_to = 'entries', null=True, blank=True)

	objects = EntryQuerySet.as_manager()

	entries = models.Manager()

	def __unicode__(self):
		return self.title

	def url_image(self):
		if not self.image:
			return None
		else:
			return "http://localhost:8000/media/%s" % self.image