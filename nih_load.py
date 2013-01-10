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

    print xml.getroot()
