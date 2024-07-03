from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    COURSE_CHOICE = [
        (1, 'Первый курс'),
        (2, 'Второй курс'),
        (3, 'Третий курс'),
        (4, 'Четвертый курс'),
        (5, 'Пятый курс')
    ]

    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True, verbose_name='Фотография')
    course = models.IntegerField(choices=COURSE_CHOICE, verbose_name='Курс', default=5)

    # date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
