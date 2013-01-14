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
    image = name = pmhid = caption = alt_text = related_terms = None
    
    if el.tag == 'image':
        name = el.get('name')
        image = 'originals/' + el.get('name')
        for child in el:
            if child.tag == 'pmhid':
                pmhid = child.text.encode('utf8')
            if child.tag == 'caption':
                if child.text:
                    caption = child.text.encode('utf8')
                else:   
                    caption = ''
            if child.tag == 'alt-text':
                if child.text:
                    alt_text = child.text.encode('utf8')
                else:
                    alt_text = ''
            if child.tag == 'related-terms':
                related_terms = etree.tostring(child)

        vol_eles = el.xpath('./*[starts-with( name(), "vol_")]')
        vol_eles_text = [etree.tostring(x) for x in vol_eles]
        blob = ''.join(vol_eles_text)

    #print "%s -  %s\n%s" % (image, pmhid, related_terms)

    image_model = Image.objects.create(image=image, caption=caption, alt_text=alt_text, 
                  name=name, pmhid=pmhid, related_terms=related_terms, blob=blob, 
                  name_of_source="PDQ", pmh_figure_source='National Institutes of Health')

