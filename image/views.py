from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Img
# Create your views here.
def home(request):
	return render(request, 'image/home.html', {})

def view_image(request):
	images = Img.objects.all()
	return render(request, 'image/view_image.html', {'images':images})

def create_image(request):
	if request.method=='POST':
		name = request.POST.get('name')
		img_file = request.FILES.get('image_url')

		Img.objects.create(
			name = name,
			img_file = img_file
		)

		return redirect('view_image')
	return render(request, 'image/image_form.html', {})