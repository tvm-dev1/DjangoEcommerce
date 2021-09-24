# Generated by Django 3.2.7 on 2021-09-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('deposit', 'Depósito'), ('pagseguro', 'PagaSeguro'), ('paypal', 'PayPal')], default='deposit', max_length=20, verbose_name='Opção de Pagamento'),
        ),
    ]
