# Generated by Django 4.2.3 on 2023-10-20 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_instance_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cluster',
            old_name='configurations',
            new_name='configuration',
        ),
    ]