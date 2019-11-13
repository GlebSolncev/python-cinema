from django.contrib import admin
from .models import Pages, Components, Comments
from cinema.settings import MEDIA_URL

admin.site.register(Pages)

@admin.register(Components)
class ComponentsAdmin(admin.ModelAdmin):
    readonly_fields = ["headshot_image"]

    def headshot_image(self, obj):
        from django.utils.html import format_html
        if(obj.image):
            return format_html(
                '<img src="{}/{}" width="72" height="72">',
                MEDIA_URL,
                obj.image,
            )
    headshot_image.short_description = "Вид изображения"


admin.site.register(Comments)
