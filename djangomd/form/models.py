from django.db import models
from django.utils import timezone


class Articles(models.Model):
    source =  models.CharField(max_length=200)
    publication_date = models.DateTimeField(
            blank=True, null=True)
    episode =  models.CharField(max_length=200)
    number = models.IntegerField
    pages = models.IntegerField
    number_of_pages = models.IntegerField
    title =  models.CharField(max_length=200)
    url =  models.CharField(max_length=200)
    scan_type =  models.CharField(max_length=200)
    attachement = models.CharField(max_length=200)
    download_available = models.BinaryField
    scanned = models.BinaryField
    authors =  models.CharField(max_length=200)

    def publish(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title