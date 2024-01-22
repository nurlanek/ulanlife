from django.db import models

# Create your models here.
class Material(models.Model):
    class Meta:
            verbose_name_plural = ('Материалы')
    name = models.CharField(max_length=255, verbose_name='Наименование')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return self.name

class MaterialTransaction(models.Model):
    class Meta:
            verbose_name_plural = ('Транзакция материалов')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Материал')
    quantity_change = models.IntegerField(verbose_name='Изменение количества')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Временная метка')

    def __str__(self):
        return f"{self.material.name} - {self.quantity_change}"