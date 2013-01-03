from django.db import models

# Create your models here.
class Image(models.Model):
    original_image = models.ImageField()
    new_filename = models.CharField(max_length=100, help_text="The new filename")
