# Generated by Django 3.1.5 on 2023-05-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestaquote',
            name='state',
            field=models.CharField(max_length=30),
        ),
    ]