from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from .models import Review


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render (request, 'home.html', {'greeting':'Hello'})

def book_detail(request, book_id):
    #return HttpResponse(f'Your book id is {book_id}')
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def book_list(request):
    #return HttpResponse(f'Your book id is {book_id}')
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_detail.html', {'review': review})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def book_review_list(request, book_id):
    reviews = Review.objects.filter(book=book_id)
    return render(request, 'book_review_list.html', {'reviews': reviews})

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text})







