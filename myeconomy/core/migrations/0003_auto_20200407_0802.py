# Generated by Django 2.2.6 on 2020-04-07 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200407_0754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailytransaction',
            old_name='entered_date',
            new_name='date',
        ),
    ]
