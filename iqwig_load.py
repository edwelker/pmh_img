import os 
import sys

sys.path.insert(0, '/home/welkere/python')
sys.path.insert(0, '/home/welkere/python/pmh_img')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pmh_img.settings'

from images.models import Image
from lxml import etree

parser = etree.XMLParser()
xml = etree.parse('import/iqwig.xml')

for el in xml.getroot():
    image = name = pmhid = pmh_figure_source = None
    alt_text = caption = ''

    if el.tag == 'image':
        image = 'originals/iqwig/' + el.get('name')
        name = el.get('name')
        for child in el:
            if child.tag == 'pmhid':
                pmhid = child.text.encode('utf8')
            elif child.tag == 'caption':
                if child.text:
                    caption = child.text.encode('utf8')
            elif child.tag == 'alt-text':
                if child.text:  
                    alt_text = child.text.encode('utf8')

    #print "%s - %s - %s - %s\n" % (name, pmhid, alt_text, caption)

    try:
        img = Image.objects.get(image=image)

        img.pmhid += ', ' + pmhid
        img.caption += ', ' + caption
        img.alt_text += ', ' + alt_text
        img.save()

    except Image.DoesNotExist:
        image_model = Image.objects.create(image=image, caption=caption, alt_text=alt_text,
                      name = name, pmhid=pmhid, name_of_source='IQWiG',
                      pmh_figure_source='Institute for Quality and Efficiency in Health Care')
