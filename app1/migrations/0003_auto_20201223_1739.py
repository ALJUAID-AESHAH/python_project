# Generated by Django 2.2.4 on 2020-12-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20201223_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='security_code',
            field=models.IntegerField(null=True),
        ),
    ]
