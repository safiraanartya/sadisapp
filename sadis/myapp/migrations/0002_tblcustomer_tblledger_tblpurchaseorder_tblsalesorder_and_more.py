# Generated by Django 5.1.1 on 2024-11-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblCustomer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('retail_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tbl_customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblLedger',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('credit', models.IntegerField(blank=True, null=True)),
                ('debit', models.CharField(blank=True, max_length=255, null=True)),
                ('information', models.CharField(blank=True, max_length=255, null=True)),
                ('nomor_so', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_ledger',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblPurchaseOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_name', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('total_price', models.CharField(blank=True, max_length=255, null=True)),
                ('nomor_po', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_purchase_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblSalesOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('total_price', models.CharField(blank=True, max_length=255, null=True)),
                ('information', models.CharField(blank=True, max_length=255, null=True)),
                ('nomor_so', models.CharField(blank=True, max_length=255, null=True)),
                ('buy_price', models.CharField(blank=True, max_length=255, null=True)),
                ('profit', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_sales_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblVendor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('contract_period', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tbl_vendor',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='tbluser',
            options={'managed': False},
        ),
    ]
