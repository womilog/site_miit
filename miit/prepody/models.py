from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse

from users.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Prepod.Status.PUBLISHED)


class Prepod(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    POST_CHOICES = [
        ('Профессор', 'Профессор'),
        ('Доцент', 'Доцент'),
        ('Старший преподаватель', 'Старший преподаватель'),
        ('Ассистент', 'Ассистент'),
        ('Старший научный сотрудник', 'Старший научный сотрудник'),
        ('Ведущий инженер', 'Ведущий инженер'),
    ]

    slug = models.SlugField(max_length=100, blank=False, unique=True, verbose_name='url препода')
    name = models.CharField(max_length=255, blank=False, verbose_name='ФИО препода', db_index=True,
                            validators=[
                                MinLengthValidator(5, message='Минимум 5 символов'),
                                MaxLengthValidator(100, message='Максимум 100 символов'),
                            ])

    age = models.IntegerField(verbose_name='Возраст препода')
    post = models.CharField(max_length=40, choices=POST_CHOICES, blank=False, verbose_name='Звание')
    nickname = models.CharField(max_length=255, verbose_name='Кликуха', blank=True)
    phrases = models.CharField(max_length=255, verbose_name='Крутые фразы(через зарятую)')
    content = models.TextField(verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='photos_prepodov/%Y/%m/%d/', default=None,
                              blank=True, verbose_name='Фото препода')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    cat = models.ForeignKey('PrepodCategory', on_delete=models.PROTECT, related_name='posts', verbose_name='Категории')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Препод'
        verbose_name_plural = 'Преподы'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['time_create'])
        ]

    def get_absolute_url(self):
        return reverse('prepody_post', kwargs={'post_slug': self.slug})


class PrepodCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('prepody_cat', kwargs={'cat_slug': self.slug})


class PrepodComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='комментатор')
    prepod = models.ForeignKey(Prepod, on_delete=models.DO_NOTHING, verbose_name='препод')
    content = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return f'комментраций пользователя {self.user.username} на препода {self.prepod.name}'