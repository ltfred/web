# Generated by Django 2.1.4 on 2020-03-09 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_articlelabel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlelabel',
            name='article',
        ),
        migrations.AddField(
            model_name='articledetail',
            name='article',
            field=models.ManyToManyField(related_name='labels', to='article.ArticleLabel'),
        ),
    ]
