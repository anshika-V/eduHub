# Generated by Django 3.0.6 on 2020-07-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='fer_data',
            field=models.TextField(default=''),
        ),
    ]