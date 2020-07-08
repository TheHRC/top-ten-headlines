from django.db import models
from django.conf import settings
# Model - headline (title, image, url)
# Model - userprofile(user, last_scrape)

class Headline(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    image_url = models.URLField(null=True)
    url = models.URLField()
    description = models.TextField(null=True, default="Oops! No Descriptions...")


    def __str__(self):
        return self.title[:15]


class UserProfile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_scrape = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.user, self.last_scrape)