from django.db import models
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

#helper method
def generate_link(image):
    return u"<a href='%s' target='_blank'>%s</a>" % (image.url, image.url.split('/')[-1])
    

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='originals')

    name = models.CharField(blank=True, unique=True, max_length=150, help_text="The new PMH name of the image, keeping '.jpg'.", verbose_name="PMH filename")
    pmhid = models.CharField(blank=True, max_length=40)

    included = models.BooleanField(help_text="Check if the image should be included in PMH", verbose_name='Include?')

    alt_text = models.TextField(blank=True, help_text="A short caption representing the image that will go in the img's 'alt' attribute.")
    caption = models.TextField(blank=True)
    source_url = models.URLField(blank=True, help_text="URL to the original source of the image.")
    orig_figure_source = models.TextField(blank=True, verbose_name="Original Figure Source", help_text="The credit/source line required by the original image owner.")
    pmh_figure_source = models.TextField(blank=True, verbose_name="PMH Figure Source text", help_text="A different version of the credit/source line that we want to display on the PMH topic page itself.")

    name_of_source = models.CharField(max_length=50, help_text="The name of the place the image came from.")

    #all of the extra XML information (starting with vol_ for PDQ) that should not be displayed, but be output later.
    blob = models.TextField()

    related_terms = models.TextField()

    #The alternate sizes of the images
    medium_thumb = ImageSpecField([ResizeToFit(width=300, height=400)], image_field='image', cache_to='medium_thumbs')
    thumbnail = ImageSpecField([ResizeToFill(130, 130)], image_field='image', cache_to='thumbnails')

    def img_thumb(self):
        if self.image:
            #this is hacky, need to reverse lookup the image
            return u'<a href="%s/"><img src="%s" /></a>' % (self.id, self.thumbnail.url)
        else:
            return u'(No image)'

    img_thumb.short_description = 'Thumbnail'
    img_thumb.allow_tags = True

    def orig_filename(self):
        return generate_link(self.image)

    orig_filename.short_description = "Original (full size)"
    orig_filename.allow_tags = True

    def med_url(self):
        return generate_link(self.medium_thumb) 
    
    med_url.short_description = "Medium Thumbnail"
    med_url.allow_tags = True

    def complete(self):
        return all((self.orig_figure_source, self.pmh_figure_source, self.source_url, self.alt_text))

    complete.short_description = 'Are all fields complete?'

    def __unicode__(self):
        return u"%s" % self.image.url.split('/')[-1]

    class Meta:
        ordering = ['-included']


class TopicPage(models.Model):
    topic = models.CharField(max_length=150,blank=True, help_text="The name of the topic")
    mesh_codes = models.CharField(max_length=200, blank=True, help_text="A comma separated list of terms this image belongs to.")
    image = models.ForeignKey(Image) 
