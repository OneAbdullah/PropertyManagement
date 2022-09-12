# Generated by Django 3.2 on 2022-08-24 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprt_number', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('phone_nmber', models.CharField(blank=True, max_length=50, null=True)),
                ('type_of', models.CharField(blank=True, max_length=300, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('contract_number', models.CharField(blank=True, max_length=300, null=True)),
                ('elect_number', models.CharField(blank=True, max_length=300, null=True)),
                ('note', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='invoice_owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('payment_method', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_of_transfer', models.CharField(blank=True, max_length=300, null=True)),
                ('transfer_date', models.DateField(blank=True, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('today_date', models.DateField(auto_now_add=True)),
                ('remaining_amount', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, max_length=2000, null=True)),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.apartment')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.invoice_owner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.invoice_owner')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.building'),
        ),
    ]
