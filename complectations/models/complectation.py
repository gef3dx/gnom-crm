from django.db import models
from complectations.utils import slugify
from users.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField

# Модель комплектации
class Complectation(models.Model):
    name = models.CharField(
        verbose_name="Имя Комплектации",
        max_length=50
    )
    adress = models.CharField(
        verbose_name="Адрес заказчика",
        max_length=150
    )
    phone = PhoneNumberField(
        verbose_name="Телефон заказчика",
        null=False,
        blank=False,
        unique=True
    )
    slug = models.SlugField(
        verbose_name="Ссылка на комплектацию",
        max_length=20,
        unique=True,
        help_text="**Можно использовать только латинские буквы"
    )
    date_create = models.DateField(
        verbose_name="Дата создания коплектации",
        auto_now=True
    )
    users = models.ManyToManyField(
        CustomUser,
        verbose_name="Доступ пользователей к комплектации"
    )
    balance = models.IntegerField(
        verbose_name="Баланс",
        default=0
    )
    procent = models.IntegerField(
        verbose_name="Процент",
        default=0
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/complectations/{self.slug}/"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        verbose_name = "Комплектация"
        verbose_name_plural = "Комплектации"