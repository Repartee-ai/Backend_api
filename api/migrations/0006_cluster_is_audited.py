# Generated by Django 4.2.3 on 2023-10-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_invoice_provider_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='is_audited',
            field=models.BooleanField(default=False),
        ),
    ]