from django.db import models
from complectations.models.complectation import Complectation
from users.models import CustomUser


# Модель поступления
class Receipts(models.Model):
    name = models.CharField(
        verbose_name="Название поступления",
        max_length=250
    )
    discription = models.TextField(
        verbose_name="Описание поступления",
        blank=True,
        null=True
    )
    date_create = models.DateField(
        verbose_name="Дата поступления"
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Сумма поступления",
        default=0
    )
    complectation = models.ForeignKey(
        Complectation,
        verbose_name="Выберите комплектацию",
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        CustomUser,
        verbose_name="Добавил поступление",
        on_delete=models.CASCADE
    )

    # def get_absolute_url(self):
    #     return reverse('receiptsfromcomplet', args=[self.slug])

    @property
    def formatted_date_create(self):
        return self.date_create.strftime("%d.%m.%Y") if self.date_create else None

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Поступление средств"
        verbose_name_plural = "Пуступления средств"