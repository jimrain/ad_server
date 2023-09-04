import os
import random

from django.shortcuts import render

from django.http import HttpResponse, FileResponse


def index(request):
    # content = open('AdServer/emotions_vast.xml', 'rb')
    # return HttpResponse(content, content_type='application/xml')
    tag_list = ["Audi_vast.xml", "Dog_vast.xml", "Doritos_vast.xml", "Gatorade_vast.xml", "KitKat_vast.xml",
                "Milk_vast.xml", "Naturo_vast.xml", "Nike_vast.xml", "Pringles_vast.xml", "SugarBites_vast.xml"]
    vast_tag = random.choice(tag_list)
    filepath = os.path.join('static', 'AdServer/' + vast_tag)
    return FileResponse(
        open(filepath, 'rb'),
        content_type='application/xml'
    )
