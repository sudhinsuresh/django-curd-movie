from django.shortcuts import render
from .models import Movie
from django.views.generic import ListView,DeleteView,UpdateView,DetailView
from django.shortcuts import redirect
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
#     k=Movie.objects.all()
#     return render(request,"home.html",{'b':k})

# def view(request,p):
#     b=Movie.objects.get(id=p)
#     return render(request,'view.html',{'b':b})

# def delete_movie(request,p):
#     b = Movie.objects.get(id=p)
#     b.delete()
#     return view(request)

class movieListview(ListView):
    model = Movie
    template_name = 'home.html'
    context_object_name = 'b'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'view.html'
    context_object_name = 'movie'

class MovieDeleteView(DeleteView):
    model =Movie
    template_name='delete.html'
    success_url=reverse_lazy('movie:index')





    

