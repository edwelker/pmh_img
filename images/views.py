from django.shortcuts import render_to_response
# Create your views here.
from models import Image

def home(request):
    return render_to_response('output.xml', {'images': Image.objects.filter(included=True).order_by('new_filename')},  mimetype="text/xml")
