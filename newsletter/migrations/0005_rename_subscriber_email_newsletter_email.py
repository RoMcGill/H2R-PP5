# Generated by Django 3.2 on 2022-11-19 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20221119_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='subscriber_email',
            new_name='email',
        ),
    ]
