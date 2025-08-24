from django.shortcuts import render, redirect
from .models import Photo, Video
from .forms import PhotoForm

def home(request):
    videos= Video.objects.all()
    photos = Photo.objects.all().order_by('-uploaded_at')[:3]  # 3 photos preview
    return render(request, "home.html", {
        'videos': videos,
        "photos": photos
    })

def about(request):
    return render(request, "about.html")

def timeline(request):
    return render(request, "timeline.html")

def gallery(request):
    photos = Photo.objects.all()
    form=PhotoForm()
    return render(request, "gallery.html", {"photos": photos, "form": form})


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})