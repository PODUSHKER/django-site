# Generated by Django 3.2.20 on 2023-09-11 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_to_die', models.DateTimeField(verbose_name='Время удаления')),
                ('uuid', models.UUIDField(unique=True, verbose_name='Уникальный код')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Письмо подтверждения',
                'verbose_name_plural': 'Письма подтверждения',
            },
        ),
    ]
