# Generated by Django 4.2 on 2024-03-17 15:44

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_user_tariff'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffs',
            name='description_en',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Tariff description'),
        ),
        migrations.AddField(
            model_name='tariffs',
            name='description_ru',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Tariff description'),
        ),
        migrations.AddField(
            model_name='tariffs',
            name='name_en',
            field=models.CharField(blank=True, default='Tariff 1', max_length=64, null=True, unique=True, verbose_name='Tariff Name'),
        ),
        migrations.AddField(
            model_name='tariffs',
            name='name_ru',
            field=models.CharField(blank=True, default='Tariff 1', max_length=64, null=True, unique=True, verbose_name='Tariff Name'),
        ),
        migrations.AddField(
            model_name='tgbotsnippet',
            name='main_menu_text_en',
            field=wagtail.fields.RichTextField(null=True, verbose_name='Main menu text'),
        ),
        migrations.AddField(
            model_name='tgbotsnippet',
            name='main_menu_text_ru',
            field=wagtail.fields.RichTextField(null=True, verbose_name='Main menu text'),
        ),
        migrations.AddField(
            model_name='tgbotsnippet',
            name='welcome_message_en',
            field=wagtail.fields.RichTextField(null=True, verbose_name='Welcome message on tg bot'),
        ),
        migrations.AddField(
            model_name='tgbotsnippet',
            name='welcome_message_ru',
            field=wagtail.fields.RichTextField(null=True, verbose_name='Welcome message on tg bot'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='currency',
            field=models.IntegerField(choices=[(1, 'Ruble ₽'), (2, 'Euro €'), (3, 'Dollar $')], verbose_name='Purpose of the request'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='uses',
            field=models.PositiveIntegerField(default=0, verbose_name='Uses in the tariff'),
        ),
    ]
