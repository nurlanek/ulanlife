from django.db import models

class Product(models.Model):
    class Meta:
            verbose_name_plural = 'Продукция'
            #db_table = 'Продукция'
    name = models.CharField(max_length=255, verbose_name='Наименование')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    condition = models.CharField(max_length=100, choices=[('good', 'Good'), ('damaged', 'Damaged')], verbose_name='состояние')

    def __str__(self):
        return self.name

class Order(models.Model):
    class Meta:
            verbose_name_plural = ('Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукция')
    quantity = models.IntegerField(verbose_name='Количество')
    customer_name = models.CharField(max_length=255, verbose_name='Клиент')
    shipping_address = models.TextField(verbose_name='Адрес достваки')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    is_shipped = models.BooleanField(default=False, verbose_name='Отправка')

    def __str__(self):
        return str(self.product)
