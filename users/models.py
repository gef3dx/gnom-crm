from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("Сотрудник", "Сотрудник"),
        ("Прораб", "Прораб"),
        ("Клиент", "Клиент"),
    ]

    objects = UserManager()

    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    phone = models.CharField(verbose_name="Телефон", max_length=15, unique=True)
    role = models.CharField(verbose_name="Роль пользователя", max_length=15, default="Клиент", choices=ROLE_CHOICES,
                            help_text="Выберите роль пользователю для работы с строительными объектами")
    bonus = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Бонусы")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.first_name} - {self.email} - {self.last_name}"

    class Meta:
        ordering = ['-id']
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
