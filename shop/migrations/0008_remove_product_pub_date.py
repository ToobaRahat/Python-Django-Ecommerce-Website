# Generated by Django 3.0.1 on 2020-01-14 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200114_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
    ]
