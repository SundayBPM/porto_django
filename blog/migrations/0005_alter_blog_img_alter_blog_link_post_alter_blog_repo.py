# Generated by Django 5.1.3 on 2024-11-29 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_img_blog_link_post_blog_repo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='link_post',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='repo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
