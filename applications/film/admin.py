from django.contrib import admin
from .models import Films, Halls, Session
from cinema.settings import MEDIA_URL
from django.utils.html import format_html
from django.urls import reverse


# admin.site.register(Films)

@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    # http://127.0.0.1:8000/admin/film/halls/2/change/
    list_display = (
        'headshot_image',
        'title',
        'time_work',
        'slug_link',
        'status',
    )
    list_display_links = ('title', 'headshot_image')

    readonly_fields = ['headshot_image']


    def slug_link(self, obj):
        return format_html('<a href="{}">SEE</a>',
           reverse('film:index', args=[obj.slug])
        )

    def headshot_image(self, obj):
        if (obj.image):
            return format_html(
                '<img src="{}/{}" width="72" height="72">',
                MEDIA_URL,
                obj.image,
            )

    headshot_image.short_description = "Вид изображения"


admin.site.register(Halls)
admin.site.register(Session)
