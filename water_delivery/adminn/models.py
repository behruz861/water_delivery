from django.db import models

class Bottle(models.Model):
    quantity = models.PositiveIntegerField(verbose_name='Кол-во воды в наличии')

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Заказчик')
    order_date = models.DateField(verbose_name='Дата заказа')
    status = models.CharField(max_length=50, verbose_name='Статус')
class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    is_busy = models.BooleanField(default=False, verbose_name='Занят')
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
class Revenue(models.Model):
    date = models.DateField(verbose_name='Дата')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
class DashboardData(models.Model):
    bottles = models.ForeignKey(Bottle, on_delete=models.CASCADE, verbose_name='Кол-во воды в наличии')
    current_orders = models.ManyToManyField(Order, verbose_name='Текущие заказы', related_name='current_orders')
    completed_orders = models.ManyToManyField(Order, related_name='completed_order', verbose_name='История заказов')
    employees = models.ManyToManyField(Employee, verbose_name='Сотрудники')
    customers = models.ManyToManyField(Customer, verbose_name='Клиенты')
    daily_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Выручка за день')
