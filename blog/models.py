from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	user = models.ForeignKey('auth.User')
	title = models.CharField(max_length=30)
	image = models.CharField(max_length=100)
	text = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def build_article(self):
		url_str = 'article/{}'.format(self.id)
		return url_str

class projects(models.Model):
	title = models.CharField(max_length=40)
	description = models.TextField()
	image = models.CharField(max_length=100)