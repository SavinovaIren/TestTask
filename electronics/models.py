from django.db import models


"""
Задолженность перед поставщиком в денежном выражении с точностью до копеек;
Время создания (заполняется автоматически при создании)."""


# Create your models here.
class Product(models.Model):
    title = models.CharField(verbose_name='Название продукта', max_length=50)
    model = models.CharField(verbose_name='Название модели', max_length=50)
    date_release = models.DateField(verbose_name='Дата выхода продукта на рынок', auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title


class Company(models.Model):
    choices = ((0, 'Завод'),
               (1, 'Розничная сеть'),
               (2, 'Индивидуальный предприниматель'))
    title = models.CharField(verbose_name='Название компании', max_length=50, unique=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    country = models.CharField(verbose_name='Название страны', max_length=50)
    city = models.CharField(verbose_name='Название города', max_length=50)
    street = models.CharField(verbose_name='Название улицы', max_length=100)
    house_number = models.CharField(verbose_name='Номер дома', max_length=50)
    products = models.ManyToManyField(Product, related_name='electronics')
    provider = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.SET_NULL,
                                 related_name='traders', null=True, blank=True)
    hierarchy = models.SmallIntegerField(verbose_name='Тип компании', choices=choices)
    debt = models.DecimalField(verbose_name='Задолжность', max_digits=20, decimal_places=2, default=0)
    public_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



