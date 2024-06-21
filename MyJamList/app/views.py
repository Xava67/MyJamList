"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.http import FileResponse, Http404
from django.contrib.staticfiles import finders
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SongForm, UpdateSongForm
from .models import Songs
from django.core.files.storage import default_storage, FileSystemStorage
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required

def pdf_view(request):
    file_path = finders.find('app/pdfs/Guitar basics.pdf')
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'About',
            'message':'About the page',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Project details',
            'message':'All important information regarding this project',
            'year':datetime.now().year,
        }
    )

def simple_upload(request):
    # return HttpResponse("<H2>Upload</H2>")
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location="ciscotest/uploadedmedia")
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'about.html', {'uploaded_file_url': uploaded_file_url,"fileupload":"File uploaded successfully"})
    return render(request, 'about.html')



@login_required
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user
            song.save()
            return redirect('my_list')  # Replace with your view name
    else:
        form = SongForm()
    return render(request, 'app/upload_song.html', {'form': form})

@login_required
def plan_to_learn(request):
    songs = Songs.objects.filter(rating=0, user=request.user);
    return render (request, 'app/plan_to_learn.html', {'songs': songs,'title':'Plan to learn', 'message':'Songs you plan to learn in the future'})

@login_required
def learning(request):
    songs = Songs.objects.filter(rating__in=[1, 2], user=request.user)
    return render (request, 'app/learning.html', {'songs': songs,'title':'Learning', 'message':'Songs you are currently learning.'})

@login_required
def mastering(request):
    songs = Songs.objects.filter(rating__in=[3, 4], user=request.user)
    return render (request, 'app/mastering.html', {'songs': songs,'title':'Mastering', 'message':'Songs you have a higher comprehension of.'})

@login_required
def mastered(request):
    songs = Songs.objects.filter(rating=5,user=request.user);
    return render (request, 'app/mastered.html', {'songs': songs,'title':'Mastered', 'message':'Songs you have fully memorised.'})

@login_required
def my_list(request):
    songs = Songs.objects.filter(user=request.user)
    return render(request, 'app/my_list.html', {'songs': songs,'title':'MyList', 'message':'Your list dshboard','ratings':[0,1,2,3,4,5],})

@login_required
def update_song(request):
    if request.method == 'POST':
        form = UpdateSongForm(request.POST, user=request.user)
        if form.is_valid():
            song = form.cleaned_data['title']
            rating = form.cleaned_data['rating']
            song.rating = rating
            song.save()
            return redirect('my_list')
    else:
        form = UpdateSongForm(user=request.user)
    return render(request, 'app/update_song.html', {'form': form})
