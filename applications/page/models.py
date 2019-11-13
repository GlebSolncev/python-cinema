from django.db import models
from datetime import datetime
from django.contrib import admin


class Pages(models.Model):
    slug = models.SlugField('ЧПУ', max_length=50, unique=True, null=False)  # CharField
    title = models.CharField('Заголовок страницы', max_length=100, null=False)
    home_page = models.BooleanField('Стартовая страница', default=False)
    allow_comment = models.BooleanField('Разрешить ставить комментарий', default=False)
    created_at = models.DateTimeField('Дата публикации', default=datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страницa'
        verbose_name_plural = 'Страницы'


class Components(models.Model):
    page = models.ForeignKey('Pages', on_delete=models.CASCADE) # _id
    title = models.CharField('Заголовок компонента', max_length=50, null=False)
    name = models.CharField('Название компонента', max_length=50, null=False, unique=True)
    value = models.TextField('Значения', default=None, null=True, blank=True)
    image = models.ImageField('Изображение', default=None, null=True, blank=True, upload_to='%Y/%m/%d/')

    def image_tag(self):
        from django.utils.html import format_html
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.title,
            self.name,
        )
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'

    class ComponentsAdmin(admin.ModelAdmin):
        list_display = ('__str__', 'image_tag')


class Comments(models.Model):
    page_id = models.ForeignKey('Pages', on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=50, null=False)
    value = models.TextField('Комментарий', null=False)
    created_at = models.DateTimeField('Дата создания', default=datetime.now())

    def __str__(self):
        return self.value[:100]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
