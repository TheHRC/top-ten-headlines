# Generated by Django 3.0.4 on 2020-03-07 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200307_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='description',
            field=models.TextField(default='Oops! No Descriptions...', null=True),
        ),
    ]
