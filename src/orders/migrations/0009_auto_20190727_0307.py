# Generated by Django 2.2.3 on 2019-07-27 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_delete_productpurchasemanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='billing_address', to='addresses.Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='billing.BillingProfile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.Cart'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='shipping_address', to='addresses.Address'),
        ),
        migrations.AlterField(
            model_name='productpurchase',
            name='billing_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billing.BillingProfile'),
        ),
        migrations.AlterField(
            model_name='productpurchase',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
    ]
