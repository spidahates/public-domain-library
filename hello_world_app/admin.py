from django.contrib import admin

from .models import Book, MediaItem


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "year", "media_type", "pd_verified")
    list_filter = ("media_type", "pd_verified")
    search_fields = ("title", "creator")


admin.site.register(Book)
