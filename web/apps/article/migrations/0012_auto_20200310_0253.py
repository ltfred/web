# Generated by Django 2.1.4 on 2020-03-10 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20200310_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='web',
            field=models.URLField(default='', null=True, verbose_name='网站'),
        ),
    ]