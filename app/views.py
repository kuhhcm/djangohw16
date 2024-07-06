from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Movie

def list_movies(request):
    books = Movie.objects.all()
    paginator = Paginator(books, 5)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'list_movies.html', {'page': page_obj})