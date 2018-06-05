from django.shortcuts import render

# Create your views here.

from .models import Gallery

def gallery(request):
	gallery = Gallery.objects
	return render(request, 'gallery/gallery.html', {'gallery':gallery})