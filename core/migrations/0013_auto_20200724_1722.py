# Generated by Django 2.2.4 on 2020-07-24 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200723_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcpsschool',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mcpsschool',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
    ]