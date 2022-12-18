from django.shortcuts import render
from django.db.models import Q
from dateutil.parser import parse as date_parse

import pandas as pd

from app.models import Author, Book, Review

def index(request):

    # searching for book title, author, and review text
    query = request.GET.get('q')
    reviews = Review.objects.filter(
            Q(book__title__icontains=query) |
            Q(book__author__name__icontains=query) |
            Q(text__icontains=query)
        )

    context = {
        'reviews': reviews
        }

    return render(request, 'app/index.html', context)


def upload_reviews(request):
    #book_reviews_path = settings.MEDIA_ROOT + '/books.xlsx'
    book_reviews_path = '/Users/dannybugingo/Desktop/src/app/static/media/books.xlsx'
    #Not best practice to hard code but oh well
    df = pd.read_excel(book_reviews_path)
    
    for review in df.itertuples():
        if Author.objects.filter(name=review.author).exists():
            print(f'Author {review.author} already exists')
        else:
            author = Author.objects.create(name=review.author)
            print (f'Added author: {review.author}')
        
        if Book.objects.filter(title=review.title).exists():
            print(f'Book {review.title} already exists')
        else:
            author = Author.objects.filter(name=review.author).first()
            try:
                date_read = date_parse(review.date_read)
            except Exception:
                date_read = None
            Book.objects.create(title=review.title, author=author, date_read=date_read, cover_image=str(review.cover_image))
            print (f'Added book: {review.title}')
        

        if Review.objects.filter(text=review.review).exists():
            print(f'Review for {review.title} already exists')
        else:
            book = Book.objects.filter(title=review.title).first()
            Review.objects.create(book=book, text=review.review, language='en')
            print (f'Added review: {review.title}')

    context = {
        'reviews': Review.objects.all(),
        }

    return render(request, 'app/upload_reviews.html', context)