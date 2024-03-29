# Generated by Django 4.2 on 2024-03-17 14:53

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('home', '0002_alter_user_tg_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tariffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Tariff 1', max_length=64, null=True, unique=True, verbose_name='Tariff Name')),
                ('description', wagtail.fields.RichTextField(blank=True, null=True, verbose_name='Tariff description')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tariff price')),
                ('currency', models.CharField(choices=[('RUBLE', 'Ruble ₽'), ('EURO', 'Euro €'), ('DOLLAR', 'Dollar $')], max_length=16, verbose_name='Purpose of the request')),
                ('uses', models.IntegerField(default=0, verbose_name='Uses in the tariff')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
            ],
        ),
        migrations.CreateModel(
            name='TgBotSnippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Bot name')),
                ('welcome_message', wagtail.fields.RichTextField(null=True, verbose_name='Welcome message on tg bot')),
                ('main_menu_text', wagtail.fields.RichTextField(null=True, verbose_name='Main menu text')),
                ('terms_of_use_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.page', verbose_name='Terms of use link')),
            ],
            options={
                'verbose_name': 'Bot settings',
                'verbose_name_plural': 'Bot settings',
            },
        ),
    ]
