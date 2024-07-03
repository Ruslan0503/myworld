from django.shortcuts import render
from .models import Picture

def home(request):
    if request.method == 'POST':
        image = request.FILES.get('image')  # Get the uploaded image file
        p = Picture(image=image)
        p.save()
    return render(request, 'home.html', {})


def pic(request):
	picts = Picture.objects.all()
	context = {
	  'picts':picts,
	}
	return render(request, 'picts.html', context)