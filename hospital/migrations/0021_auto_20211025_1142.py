# Generated by Django 3.2.7 on 2021-10-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_auto_20211025_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
