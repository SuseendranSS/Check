from django.shortcuts import render
from .models import ImageModel

def image_list(request):
    images = ImageModel.objects.all()
    return render(request, 'home/image_list.html', {'images': images})
