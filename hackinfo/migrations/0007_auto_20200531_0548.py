# Generated by Django 3.0 on 2020-05-31 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackinfo', '0006_auto_20200531_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammemberdetail',
            name='contact1',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='teammemberdetail',
            name='contact2',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='teammemberdetail',
            name='contact3',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='teammemberdetail',
            name='contact4',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='teammemberdetail',
            name='contact5',
            field=models.CharField(max_length=15),
        ),
    ]
