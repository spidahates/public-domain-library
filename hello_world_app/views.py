from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("<h1>Hello World!</h1><p>Public Domain Library</p>")

from django.shortcuts import render, redirect
from .models import Book


def book_catalog(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        description = request.POST.get("description", "").strip()

        if title and author:
            Book.objects.create(
                title=title,
                author=author,
                description=description
            )
            return redirect("book_catalog")

    query = request.GET.get("q", "").strip()
    books = Book.objects.all().order_by("title")

    if query:
        from django.db.models import Q
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

    return render(request, "book_catalog.html", {
        "books": books,
        "query": query
    })
