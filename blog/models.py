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