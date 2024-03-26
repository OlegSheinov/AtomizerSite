# Generated by Django 4.2 on 2024-03-26 15:23

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_tgbotsnippet_success_payment_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tgbotsnippet',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, max_length=1024, null=True, verbose_name='Bot description'),
        ),
        migrations.AddField(
            model_name='tgbotsnippet',
            name='description_en',
            field=wagtail.fields.RichTextField(blank=True, max_length=1024, null=True, verbose_name='Bot description'),
        ),
        migrations.AddField(
            model_name='tgbotsnippet',
            name='description_ru',
            field=wagtail.fields.RichTextField(blank=True, max_length=1024, null=True, verbose_name='Bot description'),
        ),
    ]
