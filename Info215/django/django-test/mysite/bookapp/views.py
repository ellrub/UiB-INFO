from django.shortcuts import render
from .models import Post

# Create your views here.
def books(request):
    books = Post.objects.all()
    context = {
        'books': books
    }

    return render(request, 'bookstore.html', context)