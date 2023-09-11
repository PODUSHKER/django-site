from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse

import store.settings


# Create your models here.

class User(AbstractUser):
    image = models.FileField(blank=True, verbose_name='Изображение')
    email_is_verify = models.BooleanField(default=False, verbose_name='Подтверждение почты')


class EmailVerifyMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_to_die = models.DateTimeField(verbose_name='Время удаления')
    uuid = models.UUIDField(unique=True, verbose_name='Уникальный код')

    class Meta:
        verbose_name = 'Письмо подтверждения'
        verbose_name_plural = 'Письма подтверждения'

    def __str__(self):
        return f'Message {self.created} for {self.user}'

    def send_verify_message(self):

        subject = 'Письмо подтверждения почты!'
        url = store.settings.DOMAIN_NAME + reverse('users:verify_email', kwargs={'email': self.user.email, 'code': self.uuid})
        print(url)
        text = f'Здравствуйте {self.user.username}, для подтверждения почты нажмите на ссылку ниже:\n{url}'
        email_from = store.settings.EMAIL_HOST_USER
        email_to = self.user.email

        send_mail(subject, text, email_from, [email_to])