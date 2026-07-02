from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='shirts/', blank=True, null=True)

    class Meta:
        verbose_name = 'Camiseta'
        verbose_name_plural = 'Camisetas'

    def __str__(self):
        return self.title
