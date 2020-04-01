# Generated by Django 3.0.1 on 2020-01-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customization',
            fields=[
                ('cus_id', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=5000)),
                ('custype', models.CharField(default='', max_length=170)),
                ('pricerange', models.CharField(default='', max_length=170)),
                ('time', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='demo',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='technology',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=500),
        ),
    ]