from django.db import models

class Entry(models.Model):

	title = models.CharField(max_length=50)
	content = models.TextField()
	published = models.BooleanField(default = False)
	image = models.ImageField(upload_to = 'entries', null=True, blank=True)

	def __unicode__(self):
		return self.title