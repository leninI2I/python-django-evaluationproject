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
            # return HttpResponse('Image uploaded successfully!')
            #return HttpResponseRedirect('starting-page')
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
    imadet = get_object_or_404(uploadimages, slug=slug)
    detailedimage = {
        "title":imadet.title,
        "image":imadet.imageupload,
        "description": imadet.description,
        "category":imadet.category,
        "uploadedby":imadet.uploaded_by,
        "uploadeddate":imadet.uploaded_date
    }

    redirect_path = reverse("search-page", args=[imadet.category])
    return HttpResponseRedirect(redirect_path)
    # return render(request,'image-detail.html', {
    #     "title":imadet.title,
    #     "image":imadet.imageupload,
    #     "description": imadet.description,
    #     "category":imadet.category,
    #     "uploadedby":imadet.uploaded_by,
    #     "uploadeddate":imadet.uploaded_date
    # })

# def image_detail_new(request, slug):
#     imadet = get_object_or_404(uploadimages, slug=slug)
#     redirect_path = reverse("search-page", args=[imadet.slug])
#     return HttpResponseRedirect(redirect_path)

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
            
#             return redirect('image_list')
#     else:
#         form = ImageForm()
#     return render(request, 'upload_image.html', {'form': form})

# def image_list(request):
#     images = uploadimages.objects.all()
#     return render(request, 'image_list.html', {'images': images})

# def search_images(request):
#     query = request.GET.get('q')
#     if query:
#         images = uploadimages.objects.filter(title__icontains=query) | uploadimages.objects.filter(description__icontains=query)
#     else:
#         images = uploadimages.objects.all()
#     return render(request, 'search_images.html', {'images': images})


# def index(request):
#     if request.method == 'POST':
#         form = uploadform(request.POST)

#         if(form.is_valid()):
#             return HttpResponseRedirect('thankyou.html')
        
#     else:
#         form = uploadform()
#     context = {
#         "form":form
#         }
#     return render(request, 'base.html', context)

    

# def thankyou(request):
#     return render(request, 'thankyou.html')


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
