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
        default = 'Свяжитесь с нами для получения дополнительной информации',
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
