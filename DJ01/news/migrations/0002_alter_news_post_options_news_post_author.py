# Generated by Django 5.1.3 on 2024-11-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news_post',
            name='author',
            field=models.CharField(default='admin', max_length=50, verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
