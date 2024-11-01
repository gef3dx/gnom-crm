from django.db import models
from complectations.models import Complectation
from complectations.utils import procurements_xlsx_upload_to
from users.models import CustomUser


class Service(models.Model):
    PAYMENT_CHOICES = [
        ("Оплатил", "Оплатил"),
        ("Не оплатил", "Не оплатил"),
    ]

    MEAS_CHOICES = [
        ("шт", "штуки"),
        ("к/м", "квадратные метры"),
        ("п/м", "погоные метры"),
        ("литр", "литры"),
        ("куб", "кубы"),
        ("кг", "килограмы"),
    ]

    name = models.CharField(
        verbose_name="Имя услуги",
        max_length=50
    )
    xlsx_file = models.FileField(
        verbose_name="Excel файл сметы",
        upload_to=procurements_xlsx_upload_to,
        blank=True,
        null=True
    )
    discription = models.TextField(
        verbose_name="Описание услуги",
        blank=True,
        null=True
    )
    date_create = models.DateField(
        verbose_name="Дата добавления"
    )
    meas = models.CharField(
        verbose_name="Вид исчисления",
        max_length=8,
        default="1",
        choices=MEAS_CHOICES
    )
    count = models.DecimalField(
        max_digits=12,
        decimal_places=1,
        verbose_name="Количество",
        default=0
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Цена",
        default=0
    )
    price_all = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Цена за все",
        default=0
    )
    complectation = models.ForeignKey(
        Complectation,
        verbose_name="Выберите комплектацию",
        on_delete=models.CASCADE
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
    author = models.ForeignKey(
        CustomUser,
        verbose_name="Автор",
        on_delete=models.CASCADE
    )
    process_org = models.BooleanField(
        verbose_name="Организация процесса",
        default=False
    )
    payment_status = models.CharField(
        verbose_name="Статус оплаты",
        max_length=15,
        choices=PAYMENT_CHOICES,
        default="Не оплатил"
    )

    # def get_absolute_url(self):
    #     return reverse('servicefromcomplet', args=[self.slug])

    @property
    def formatted_date_create(self):
        return self.date_create.strftime("%d.%m.%Y") if self.date_create else None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
