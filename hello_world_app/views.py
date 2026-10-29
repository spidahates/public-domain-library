from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Book, MediaItem


def home(request):
    query = request.GET.get("q", "").strip()
    active_type = request.GET.get("type", "").strip()

    items = MediaItem.objects.all()
    if query:
        items = items.filter(
            Q(title__icontains=query) | Q(creator__icontains=query)
        )
    if active_type:
        items = items.filter(media_type=active_type)

    type_counts = {}
    for value, _label in MediaItem.MediaType.choices:
        type_counts[value] = MediaItem.objects.filter(media_type=value).count()

    return render(
        request,
        "home.html",
        {
            "items": items,
            "query": query,
            "active_type": active_type,
            "media_types": MediaItem.MediaType.choices,
            "type_counts": type_counts,
            "total_count": MediaItem.objects.count(),
        },
    )


def media_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    related = (
        MediaItem.objects.filter(media_type=item.media_type)
        .exclude(pk=item.pk)[:4]
    )
    return render(
        request, "media_detail.html", {"item": item, "related": related}
    )


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
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

    return render(request, "book_catalog.html", {
        "books": books,
        "query": query
    })
