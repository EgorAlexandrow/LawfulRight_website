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


# class Order(models.Model):
#     name = models.CharField(
#         max_length=50,
#         verbose_name='Ваше имя',
#     )
#     phone = models.CharField(
#         max_length=11,
#         verbose_name='Номер телефона',
#     )
#     problem = HTMLField(
#         verbose_name='Описание проблемы'
#     )
#     confidetial = models.BooleanField(
#         verbose_name='Согласие с политикой конфиденциальность'
#     )

#     class Meta:
#         verbose_name = 'Заявка'
#         verbose_name_plural = 'Заявка'
    
#     def __str__(self):
#         return f'{self.name}'


class Cookies(models.Model):
    cookies_title = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    cookies_text = HTMLField(
        verbose_name='Текст cookies'
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовать'
    )

    class Meta:
        verbose_name = 'Cookies'
        verbose_name_plural = 'Cookies'
    
    def __str__(self):
        return f'{self.cookies_title}'
