# Generated by Django 2.0 on 2020-04-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200407_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytransaction',
            name='updated_date',
            field=models.DateTimeField(),
        ),
    ]
