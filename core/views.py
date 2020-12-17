from django.shortcuts import render
from core.models import Album
from django.http import HttpResponse

# Create your views here.
def home(request):
    posts = Album.objects.all()
    return render(request, 'home.html', {'posts': post})


def post(request, post_id):
    post = Album.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})


def album(request):
    album = Album.objects.all()
    return render(request, 'album.html', {'posts': album})

def posted(request):
    posts = Album.objects.all()
    for post in posts:
        if post % 2 == 0:
            return render(request, """<div class="row mb-2 " >
    <div class="col-md-6">
      <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
        <div class="col p-4 d-flex flex-column position-static">
          <strong class="d-inline-block mb-2 text-primary">{{ post.title }}</strong>
          <h3 class="mb-0">{{ post.author.get_full_name }}</h3>
          <div class="mb-1 text-muted">{{ post.created_at|date:'d, M Y'}}</div>
          <p class="card-text mb-auto">{{ post.summary|safe }}</p>
          <a href="/post/{{ post.pk }}" class="stretched-link">Continue reading</a>
        </div>
        <div class="col-auto d-none d-lg-block">
          <img class="bd-placeholder-img" width="200" height="250" src="{{post.image.url}}" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/></img>

        </div>
      </div>
    </div>""",)
        return render(request, """<div class="col-md-6">
      <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
        <div class="col p-4 d-flex flex-column position-static">
          <strong class="d-inline-block mb-2 text-success">Design</strong>
          <h3 class="mb-0">Post title</h3>
          <div class="mb-1 text-muted">Nov 11</div>
          <p class="mb-auto">This is a wider card with supporting text below as a natural lead-in to additional content.</p>
          <a href="#" class="stretched-link">Continue reading</a>
        </div>
        <div class="col-auto d-none d-lg-block">
          <img class="bd-placeholder-img" width="200" height="250" src="{% static "images/pexels-pixabay-159358.jpg"%}" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"/></img>

        </div>
      </div>
    </div>
  </div>""",)