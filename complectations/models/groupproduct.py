from django.db import models
from complectations.utils import slugify

# Модель группы продуктов
class GroupProduct(models.Model):
    name = models.CharField(
        verbose_name="Имя группы",
        max_length=50
    )
    slug = models.SlugField(
        verbose_name="Ссылка на группу",
        max_length=20, unique=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        verbose_name = "Группа коплектации"
        verbose_name_plural = "Группы коплектаций"