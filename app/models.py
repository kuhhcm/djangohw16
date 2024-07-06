from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Оценка')
    year = models.IntegerField(verbose_name='Год выпуска')

    def __str__(self):
        return f"{self.name} ({self.year})"
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
