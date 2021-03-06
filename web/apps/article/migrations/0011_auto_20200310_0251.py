# Generated by Django 2.1.4 on 2020-03-10 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20200309_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecomment',
            options={'verbose_name': '文章评论', 'verbose_name_plural': '文章评论'},
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='article.ArticleDetail', verbose_name='文章'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='author',
            field=models.CharField(default=1, max_length=20, verbose_name='评论人昵称'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='content',
            field=models.TextField(default='', verbose_name='评论内容'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='email',
            field=models.CharField(default='', max_length=50, verbose_name='邮箱'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='web',
            field=models.URLField(default='', verbose_name='网站'),
        ),
        migrations.AlterModelTable(
            name='articlecomment',
            table='comment',
        ),
    ]
