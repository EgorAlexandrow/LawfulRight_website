from django.db import models

from tinymce.models import HTMLField


class Services(models.Model):
    service_title = models.CharField(
        max_length=50,
        verbose_name='Название услуги'
    )
    service_img = models.ImageField(
        upload_to='media/img/',
        verbose_name='Картинка для услуги'
    )
    text_for_popup = HTMLField(
        default='Свяжитесь с нами для получения дополнительной информации',
        verbose_name='Текст для модального окна'
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовать'
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f'{self.service_title}'


class Order(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Ваше имя',
    )
    phone = models.CharField(
        max_length=11,
        blank=False,
        null=False,
        verbose_name='Номер телефона',
    )
    email = models.EmailField(
        blank=False,
        null=False,
        verbose_name='Email'
    )
    problem = models.TextField(
        blank=False,
        null=False,
        verbose_name='Описание проблемы'
    )
    confidential = models.BooleanField(
        blank=False,
        null=False,
        verbose_name='Согласие с политикой конфиденциальность'
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'
    
    def __str__(self):
        return f'{self.name}'


class Privacy(models.Model):
    privacy_title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    privacy_text = HTMLField(
        verbose_name='Текст политики конфиденциальности'
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовать'
    )

    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'
    
    def __str__(self):
        return f'{self.privacy_title}'
