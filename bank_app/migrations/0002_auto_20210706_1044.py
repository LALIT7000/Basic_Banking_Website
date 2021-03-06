# Generated by Django 3.1.6 on 2021-07-06 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send', models.CharField(max_length=30)),
                ('receive', models.CharField(max_length=30)),
                ('amount', models.FloatField(max_length=100)),
                ('transtype', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='bmodel',
            name='balance',
            field=models.FloatField(max_length=100),
        ),
    ]
