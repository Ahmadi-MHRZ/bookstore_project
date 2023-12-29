from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    author = models.CharField(max_length=200, verbose_name=_('author'))
    description = models.TextField(verbose_name=_('description'))
    price = models.DecimalField(max_digits=6, decimal_places=3, verbose_name=_('price'))
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name=_('cover'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_('text'))
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', verbose_name=_('comments'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True, verbose_name=_('recommend'))

    def __str__(self):
        return self.text
