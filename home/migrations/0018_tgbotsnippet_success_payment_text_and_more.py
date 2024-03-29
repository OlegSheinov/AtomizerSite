# Generated by Django 4.2 on 2024-03-26 12:51

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_tariffs_currency_alter_tariffs_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='tgbotsnippet',
            name='success_payment_text',
            field=wagtail.fields.RichTextField(null=True, verbose_name='Success payment text'),
        ),
        migrations.AddField(
            model_name='tgbotsnippet',
            name='success_payment_text_en',
            field=wagtail.fields.RichTextField(null=True, verbose_name='Success payment text'),
        ),
        migrations.AddField(
            model_name='tgbotsnippet',
            name='success_payment_text_ru',
            field=wagtail.fields.RichTextField(null=True, verbose_name='Success payment text'),
        ),
    ]
