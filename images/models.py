from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='originals')
    new_filename = models.CharField(max_length=100, help_text="The new filename")

    def img_thumb(self):
        #will need to be changed to the thumbnail once generated
        if self.image:
            return u'<img src="/media/%s" />' % self.image
        else:
            return u'(No image)'

    img_thumb.short_description = 'Thumb'
    img_thumb.allow_tags = True
