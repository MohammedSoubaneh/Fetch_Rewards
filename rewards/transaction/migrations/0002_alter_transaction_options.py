# Generated by Django 4.1.2 on 2022-10-13 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('-timestamp',)},
        ),
    ]