from django.db import models


class Films(models.Model):
    slug = models.SlugField('ЧПУ', max_length=150, unique=True, null=False)
    title = models.CharField('Название фильма', max_length=150, unique=True, null=False)
    description = models.TextField('Описание', null=False)
    time_work = models.TextField('Время работы', null=False)
    image = models.ImageField('Изображение фильма', null=False, upload_to='%Y/%m/%d/')
    status = models.BooleanField('Работа фильма', default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Halls(models.Model):
    row = models.CharField('Количество по горизонтали', null=False, max_length=3)
    column = models.CharField('Количество по вертикали', null=False, max_length=3)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Session(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    hall = models.ForeignKey(Halls, on_delete=models.CASCADE)

    time = models.DateTimeField('Время', null=False)
    type = models.CharField('Тип фильма', null=False, max_length=100)

    def __str__(self):
        return str(self.film.title) + " в " + str(self.time.strftime('%H:%M'))

    class Meta:
        verbose_name = 'Сеанс'
        verbose_name_plural = 'Сеансы'
