# Generated by Django 4.2.3 on 2023-11-07 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_user_routing_number_alter_cluster_virtualization'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
