from django.shortcuts import render_to_response
# Create your views here.
from models import Image

def home(request):
    return render_to_response('output.xml', {'images': Image.objects.filter(included=True)},  mimetype="text/xml")
