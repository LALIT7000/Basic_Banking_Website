# Generated by Django 3.1.6 on 2021-07-06 05:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0002_auto_20210706_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmodel',
            name='dt',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
