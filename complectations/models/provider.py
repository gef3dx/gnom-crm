from django.db import models

# Модель поставщика
class Provider(models.Model):
    name = models.CharField(
        verbose_name="Имя поставщика",
        max_length=250
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"