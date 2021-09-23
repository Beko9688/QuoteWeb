from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name

class Quotes(models.Model):
    quote_text = models.TextField(verbose_name='Цитата')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, verbose_name='Автор')

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    def __str__(self):
        return self.quote_text[:50]
