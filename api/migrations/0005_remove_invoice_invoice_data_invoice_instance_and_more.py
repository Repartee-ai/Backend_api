# Generated by Django 4.2.3 on 2023-10-02 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_user_card_exp_remove_user_card_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_data',
        ),
        migrations.AddField(
            model_name='invoice',
            name='instance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='api.instance'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Price of the instance per hour or unit', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='total_price',
            field=models.DecimalField(decimal_places=2, help_text='Total price including tax', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='usage',
            field=models.DecimalField(decimal_places=2, help_text='Number of hours or units used', max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='credit_card',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='StripeCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_customer_id', models.CharField(max_length=255)),
                ('stripe_payment', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=255, unique=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('cpu', models.CharField(blank=True, max_length=255, null=True)),
                ('memory', models.CharField(blank=True, max_length=255, null=True)),
                ('pods', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='instance',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cluster'),
        ),
    ]