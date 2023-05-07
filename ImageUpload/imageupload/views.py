from django.shortcuts import render, redirect, get_object_or_404
from .models import uploadimages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ImageUploadForm
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        print("inside IF POST")
        if form.is_valid():
            form.save()
            print("inside save")
            return render(request, 'imageupload/success.html')
    else:
        print("else")
        form = ImageUploadForm()
    print("outside")
    return render(request, 'base.html', {'form': form})
print("completely outside")

def search(request):
    query = request.GET.get('q', '')
    images = uploadimages.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'images': images})

def image_detail(request, slug):
    query = request.GET.get('q', '')
    images = uploadimages.objects.filter(title__icontains=query)
    singleimage = next(images for image in images if image == slug)

    return render(request,'image-detail.html', {
        'image':singleimage
    })



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('login.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid email/password'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
