# Generated by Django 4.2 on 2024-03-19 17:55

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_tgbotsnippet_terms_of_use_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tgbotsnippet',
            name='terms_of_use_text',
            field=wagtail.fields.RichTextField(help_text='The link in the bot will be located under the texts', null=True, verbose_name='Terms of use text'),
        ),
        migrations.AlterField(
            model_name='tgbotsnippet',
            name='terms_of_use_text_en',
            field=wagtail.fields.RichTextField(help_text='The link in the bot will be located under the texts', null=True, verbose_name='Terms of use text'),
        ),
        migrations.AlterField(
            model_name='tgbotsnippet',
            name='terms_of_use_text_ru',
            field=wagtail.fields.RichTextField(help_text='The link in the bot will be located under the texts', null=True, verbose_name='Terms of use text'),
        ),
    ]