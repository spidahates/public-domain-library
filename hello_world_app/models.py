
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class MediaItem(models.Model):
    class MediaType(models.TextChoices):
        MOVIE = "movie", "Movie"
        TV = "tv", "TV Show"
        BOOK = "book", "Book"
        MUSIC = "music", "Music"
        AUDIOBOOK = "audiobook", "Audiobook"
        NEWSPAPER = "newspaper", "Newspaper"

    title = models.CharField(max_length=300)
    creator = models.CharField(max_length=300, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    media_type = models.CharField(
        max_length=20, choices=MediaType.choices, default=MediaType.BOOK
    )
    description = models.TextField(blank=True)
    cover_url = models.URLField(max_length=1000, blank=True)
    magnet_link = models.TextField(blank=True)
    torrent_url = models.URLField(max_length=1000, blank=True)
    source_name = models.CharField(max_length=200, blank=True)
    source_url = models.URLField(max_length=1000, blank=True)
    pd_note = models.CharField(max_length=500, blank=True)
    pd_verified = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
