# Generated by Django 3.0.7 on 2020-10-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('OutForDelivery', 'OutForDelivery')], max_length=100, null=True),
        ),
    ]
