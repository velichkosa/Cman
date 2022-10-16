from django.db import models


# Create your models here.
class Pay_status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')


class Operand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')


class Plot(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')


class Direction(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')


class Role(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    password = models.CharField(max_length=100, blank=True, verbose_name='Пароль')
    pnum = models.IntegerField(blank=True, verbose_name='Телефон')
    role = models.ForeignKey(Role, blank=True, verbose_name='Должность', on_delete=models.PROTECT)
    user_id = models.IntegerField(blank=True, verbose_name='TG')


class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')


class Provider(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    inn = models.IntegerField(blank=True, verbose_name='ИНН')
    location = models.ForeignKey(Location, verbose_name='Местонахождение', on_delete=models.PROTECT)


class Invoice(models.Model):
    provider = models.ForeignKey(Provider, verbose_name='Поставщик', on_delete=models.PROTECT)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT)
    created_at = models.DateField(editable=True, null=True, verbose_name='Дата создания')
    direction = models.ForeignKey(Direction, verbose_name='Направление', on_delete=models.PROTECT)
    plot = models.ForeignKey(Plot, verbose_name='Участок', on_delete=models.PROTECT)
    operand = models.ForeignKey(Operand, verbose_name='Обьект', on_delete=models.PROTECT)
    pay_status = models.ForeignKey(Pay_status, verbose_name='Статус оплаты', on_delete=models.PROTECT)
    pay_dock = models.FileField(upload_to='files/pay_dock/%Y/%m/%d/', verbose_name='Платежка', null=True,)
    paid_at = models.DateField(editable=True, null=True, verbose_name='Дата оплаты')
    check_file = models.FileField(upload_to='files/check_file/%Y/%m/%d/', verbose_name='Счет на оплату', null=True,)
    total_price = models.IntegerField(blank=True, verbose_name='Сумма')
    comment = models.CharField(max_length=200, verbose_name='Комментарий')
    agreement = models.BooleanField(blank=True, verbose_name='Согласование')
    agreement_at = models.DateField(editable=True, null=True, verbose_name='Дата согласования')
    invoice = models.FileField(upload_to='files/invoice/%Y/%m/%d/', verbose_name='Счет фактура', null=True)
    invoice_date = models.DateField(editable=True, null=True, verbose_name='Дата СФ')
    buh_closed = models.BooleanField(blank=True, verbose_name='Закрыт по БУХ')
