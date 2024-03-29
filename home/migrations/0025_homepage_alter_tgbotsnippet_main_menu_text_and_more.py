# Generated by Django 4.2 on 2024-03-26 17:45

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('home', '0024_alter_user_tg_first_name_alter_user_tg_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='tgbotsnippet',
            name='main_menu_text',
            field=wagtail.fields.RichTextField(help_text='\nПодсказка возможных переменных в тексте:\n\n$tariff - название тарифа юзера\n\n$tgFirstName - его имя в тг\n\n$tgId - его id в тг\n\n$tgLastName - его фамилия в тг\n\n$tgUsername - его юзернейм в тг\n\n$timeWithUs - время пользования ботом\n\n$totalUses - общее количество пользований ботом\n\n$usesLeft - оставшееся количество пользований ботом\n\n', null=True, verbose_name='Main menu text'),
        ),
        migrations.AlterField(
            model_name='tgbotsnippet',
            name='main_menu_text_en',
            field=wagtail.fields.RichTextField(help_text='\nПодсказка возможных переменных в тексте:\n\n$tariff - название тарифа юзера\n\n$tgFirstName - его имя в тг\n\n$tgId - его id в тг\n\n$tgLastName - его фамилия в тг\n\n$tgUsername - его юзернейм в тг\n\n$timeWithUs - время пользования ботом\n\n$totalUses - общее количество пользований ботом\n\n$usesLeft - оставшееся количество пользований ботом\n\n', null=True, verbose_name='Main menu text'),
        ),
        migrations.AlterField(
            model_name='tgbotsnippet',
            name='main_menu_text_ru',
            field=wagtail.fields.RichTextField(help_text='\nПодсказка возможных переменных в тексте:\n\n$tariff - название тарифа юзера\n\n$tgFirstName - его имя в тг\n\n$tgId - его id в тг\n\n$tgLastName - его фамилия в тг\n\n$tgUsername - его юзернейм в тг\n\n$timeWithUs - время пользования ботом\n\n$totalUses - общее количество пользований ботом\n\n$usesLeft - оставшееся количество пользований ботом\n\n', null=True, verbose_name='Main menu text'),
        ),
    ]
