# Generated by Django 5.0.4 on 2024-04-13 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('sold_quantity', models.IntegerField(default=0)),
                ('remaining_quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('origin', models.CharField(max_length=100)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
    ]
