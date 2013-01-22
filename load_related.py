import os
import sys

sys.path.insert(0, '/home/welkere/python')
sys.path.insert(0, '/home/welkere/python/pmh_img')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pmh_img.settings'

from images.models import Image
from lxml import etree

parser = etree.XMLParser(ns_clean=True, recover=True)
xml = etree.parse('import/pdq.xml', parser)

for el in xml.getroot():    
    image = related_terms = None
    
    if el.tag == 'image':
        image = 'originals/' + el.get('name')
        for child in el:
            if child.tag == 'related-terms':
                related_terms_array = child.xpath('.//term-id/text()')
                related_terms_array = [x.lstrip('glossary_') for x in related_terms_array]
                related_terms = '|'.join(related_terms_array)
                #related_terms = etree.tostring(child)

    if related_terms:
        Image.objects.filter(image__exact=image).update(related_terms=related_terms)
        #print "{} {}\n".format(image_model, related_terms)
