# Generated by Django 2.1.2 on 2020-12-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201230_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sample_3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='名前'),
        ),
    ]
