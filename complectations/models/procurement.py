from django.db import models
from complectations.models.complectation import Complectation
from complectations.models.provider import Provider
from complectations.utils import check_img_upload_to, procurements_xlsx_upload_to
from users.models import CustomUser


# Модель закупки
class Procurement(models.Model):
    PAYMENT_CHOICES = [
        ("Оплатил", "Оплатил"),
        ("Не оплатил", "Не оплатил"),
    ]

    name = models.CharField(
        verbose_name="Имя товара или услуги",
        max_length=50
    )
    discription = models.TextField(
        verbose_name="Описание товара или услуги",
        blank=True,
        null=True
    )
    date_create = models.DateField(
        verbose_name="Дата добавления чека"
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Сумма чека",
        default=0
    )
    procent = models.IntegerField(
        verbose_name="Процент %",
        default=0
    )
    price_procent = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Сумма наценки",
        default=0
    )
    provider = models.ForeignKey(
        Provider,
        verbose_name="Выберите поставщика",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    payment_status = models.CharField(
        verbose_name="Статус оплаты",
        max_length=15,
        choices=PAYMENT_CHOICES,
        default="Не оплатил"
    )
    image = models.ImageField(
        verbose_name="Чек",
        upload_to=check_img_upload_to,
        blank=True
    )
    xlsx_file = models.FileField(
        verbose_name="Excel файл сметы",
        upload_to=procurements_xlsx_upload_to,
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        CustomUser,
        verbose_name="Автор",
        on_delete=models.CASCADE
    )
    complectation = models.ForeignKey(
        Complectation,
        verbose_name="Выберите комплектацию", on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse('productfromcomplet', args=[self.slug])

    @property
    def formatted_date_create(self):
        return self.date_create.strftime("%d.%m.%Y") if self.date_create else None

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Закупка"
        verbose_name_plural = "Закупки"
