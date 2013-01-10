import os
import sys
from glob import glob

sys.path.insert(0, '/home/welkere/python')
sys.path.insert(0, '/home/welkere/python/pmh_img')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pmh_img.settings'

from images.models import Image
from lxml import etree

parser = etree.XMLParser(ns_clean=True, recover=True)
#get the files that we need to parse
files = glob('import/N*.xml')
for file in files:
    xml = etree.parse(file, parser)
    
    center = xml.getroot().tag

    for el in xml.getroot():
        image = name = related_terms = source_url = pmh_figure_source = None
        blob = alt_text = caption =  orig_figure_source = ''

        if el.tag == 'row':
            for child in el:
                if child.tag == 'Filename':
                    image = 'originals/' + center + '/' + child.text.encode('utf8') + '.jpg'
                elif child.tag == 'URL_for_original':
                    source_url = child.text.encode('utf8')
                elif child.tag == 'Title':
                    name = child.text.encode('utf8')
                elif child.tag == 'Description':
                    caption = child.text.encode('utf8')
                elif child.tag == 'Alternate_Text':
                    if child.text:
                        alt_text = child.text.encode('utf8')
                    else:
                        alt_text = ''
                elif child.tag == 'Display_credit_line':
                    pmh_figure_source = child.text.encode('utf8')
                elif child.tag == 'Credit_Line':
                    orig_figure_source = child.text.encode('utf8')
                elif child.text:
                    blob += etree.tostring(child)

#        print "%s      %s      %s     %s      %s      %s       %s\n\n%s\n\n\n\n" % \
#                    (image, name, source_url, caption, alt_text, pmh_figure_source, orig_figure_source, blob)

        try:
            image_model = Image.objects.create(image=image,name=name,caption=caption,source_url=source_url, \
                alt_text=alt_text,pmh_figure_source=pmh_figure_source,orig_figure_source=orig_figure_source, \
                blob=blob)
        except Exception, err:
            print "Image data error: %s, \n%s" % (err, alt_text)
