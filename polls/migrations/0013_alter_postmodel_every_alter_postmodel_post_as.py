# Generated by Django 4.1.3 on 2023-02-23 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_fbaccount_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='every',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='post_as',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=None, max_length=200),
        ),
    ]