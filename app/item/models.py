from django.db import models


from app.constants import NULLABLE

class Item(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наимменование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоймость')

    def __str__(self):
        return f'{self.name} - {self.price}$ ({self.description[:15]}...)'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)
