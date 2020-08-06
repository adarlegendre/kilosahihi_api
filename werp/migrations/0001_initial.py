# Generated by Django 2.2.7 on 2020-06-16 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=19)),
                ('id_no', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('zone', models.CharField(max_length=20)),
                ('distro_date', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Farmers',
            },
        ),
        migrations.CreateModel(
            name='FarmProduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Farm Produce',
            },
        ),
        migrations.CreateModel(
            name='FarmReturnOfficers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=49)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('id_no', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=50)),
                ('zone', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Farm Return Officers',
            },
        ),
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('zone', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Farms',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weight', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=10)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='werp.Farms')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='werp.Farmers')),
                ('fro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='werp.FarmReturnOfficers')),
                ('produce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='werp.FarmProduce')),
            ],
            options={
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
