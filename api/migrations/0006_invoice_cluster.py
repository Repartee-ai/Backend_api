# Generated by Django 4.2.3 on 2023-10-02 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_invoice_invoice_data_invoice_instance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='cluster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.cluster'),
        ),
    ]