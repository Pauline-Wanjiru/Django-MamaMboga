# Generated by Django 4.2.1 on 2023-06-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=120)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('order_id', models.PositiveIntegerField()),
            ],
        ),
    ]