# Generated by Django 4.1.4 on 2022-12-10 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import servicebook.accounts.validators
import servicebook.cars.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('AUDI', 'Audi'), ('BMW', 'BMW'), ('Ford', 'Ford'), ('VW', 'Volkswagen'), ('HONDA', 'Honda'), ('MAZDA', 'Mazda'), ('MERCEDES', 'Mercedes'), ('MITSUBISHI', 'Mitsubishi'), ('TOYOTA', 'Toyota'), ('SUBARU', 'Subaru'), ('SUZUKI', 'Suzuki'), ('JEEP', 'Jeep'), ('OPEL', 'Opel'), ('NISSAN', 'Nissan'), ('RENAULT', 'Renault'), ('Other', 'Other')], max_length=20)),
                ('model', models.CharField(max_length=20, validators=[servicebook.cars.validators.validate_string_min_2_symbols])),
                ('year_of_manufacture', models.PositiveIntegerField(blank=True, null=True, validators=[servicebook.cars.validators.validate_year_between_1970_and_2022])),
                ('engine', models.CharField(blank=True, max_length=20, null=True)),
                ('fuel', models.CharField(blank=True, max_length=20, null=True)),
                ('car_photo', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarTaxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('INSURANCE', 'Insurance'), ('INSPECTION', 'Inspection'), ('TAX', 'Tax'), ('VIGNETTE', 'Vignette'), ('Other', 'Other')], max_length=20, null=True)),
                ('valid_to', models.DateField(blank=True, null=True, validators=[servicebook.cars.validators.validate_date_is_not_in_past])),
                ('days_to_expiry', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cars.carinfo')),
            ],
        ),
        migrations.CreateModel(
            name='CarService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_service', models.DateField(blank=True, null=True, validators=[servicebook.accounts.validators.validate_date_is_not_in_future])),
                ('mileage', models.PositiveIntegerField(blank=True, null=True)),
                ('symptoms', models.CharField(blank=True, max_length=20, null=True)),
                ('root_cause', models.CharField(blank=True, max_length=20, null=True)),
                ('repair', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cars.carinfo')),
            ],
        ),
    ]