# Generated by Django 2.2.6 on 2019-10-05 10:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_app', '0011_auto_20191005_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='customer_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
