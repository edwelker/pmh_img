import os
import sys

#sys.path.insert(0, '/home/biyyalas/python')
sys.path.insert(0, '/home/welkere/python')
#sys.path.insert(0, '/home/biyyalas/python/pmh_img')
sys.path.insert(0, '/home/welkere/python/pmh_img')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pmh_img.settings'

from images.models import Image
from lxml import etree

def diff(a, b):
    return list(set(a) - set(b))

# Main driver method             
def main(argv):
    # There is no bijective (1-1) correspondence between images in zip and xml document: We recognize that all the images given
    # in the zip have to be pre-populated to the authoring interface;
    # This script is hence a best-effort attempt to ransack the xml and pre-populate
    valid_list = os.listdir('media/originals/HealthTopics')

    populated_img_list = [] # The list of images which are an intersection between images provided and xml document
    counter  = 0
    
    parser = etree.XMLParser(ns_clean=True, recover=True)
    xml = etree.parse('import/nhlbi-meta.xml', parser)

    center = 'HealthTopics'

    for el in xml.getroot():
        
        image = source_url = name = None 
        blob = alt_text = caption = ''

        if el.tag == 'file':
            for child in el:
                if child.tag == 'name': # can be jpg, png or gif
                    imgName = child.text.encode('utf8')
                    #print imgName
                    if (imgName.endswith(".jpg") or imgName.endswith(".gif") or imgName.endswith(".png")) \
                            and (imgName in valid_list) : # 1. only images 2. Should be valid 
                        image = 'originals/' + center + '/' + imgName
                        
                        # (Probably not the best way) Leveraging the 'ordering' in place for the xml. If we encounter a 'title'
                        # child later, the name is overriden.
                        # The idea is to have the name assigned to atleast image name (default)
                        name = imgName
                        populated_img_list.append(imgName) # appending to Uploaded image list 
                    else:
                        continue # Don't worry about looking into the other children if it isn't an image (psds et al)
                        
                elif child.tag == 'topic-url':
                    source_url = child.text.encode('utf8')
                elif child.tag == 'title': # Override the name
                    name = child.text.encode('utf8')
                elif child.tag == 'description':
                    caption = child.text.encode('utf8')
                elif child.tag == 'alt-text':
                    if child.text is not None:
                        alt_text = child.text.encode('utf8')
                elif child.text:
                    blob += etree.tostring(child)
            
            # At this point, if name 
        # write to database iff image is not None, (filter out the psds and other files from images)
        if image is not None:

            # The XML is inconsistent; lots of redundancy
            try:
                img  = Image.objects.get(image=image)
                counter += 1
            except Image.DoesNotExist:
                image_model = Image.objects.create(image=image,name=name,caption=caption,source_url=source_url, \
                                                   alt_text=alt_text, pmh_figure_source = 'National Heart, Lung, and Blood Institute', \
                                                   blob=blob)
               
    # Done with the xml document
    images_still_to_upload = diff(valid_list, populated_img_list)
    print "Report: There were %d duplicacies encountered. Number of images uploaded and have corresponding metadata : %d"%(counter, len(populated_img_list)-counter )
    print "Number of images to be uploaded without metadata: %d"%(len(images_still_to_upload))

    for img in images_still_to_upload:
        image = 'originals/HealthTopics/' + img
        name = img
        try:
            imag  = Image.objects.get(image=image)
            
        except Image.DoesNotExist:
            image_model = Image.objects.create(image=image,name=name, pmh_figure_source = 'National Heart, Lung, and Blood Institute')
                                                    
if __name__ == '__main__':
    sys.exit(main(sys.argv))
