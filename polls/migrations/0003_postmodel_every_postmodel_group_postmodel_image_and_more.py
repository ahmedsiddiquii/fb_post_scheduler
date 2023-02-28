# Generated by Django 4.1.3 on 2023-02-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_postmodel_delete_fbposts_delete_scehdule'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='every',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='group',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='post_as',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='time',
            field=models.TimeField(default=None),
        ),
    ]
