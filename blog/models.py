from django.db import models

# Create A Blog model
# Add the Blog app to the settings
# Create a migration
# migrate
# Add to the admin

class Blog(models.Model):
	image = models.ImageField(upload_to='images/', null=True) #title
	pub_date = models.DateTimeField(null=True) #publish date
	title = models.CharField(max_length=255, null=True) #title
	body = models.TextField(null=True) #body

	def summary(self):
		return self.body[:200]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

	def __str__(self):
		return self.title