# Generated by Django 3.2.4 on 2022-08-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.CharField(default='this text will be in the intro information on the homepage', max_length=250),
            preserve_default=False,
        ),
    ]
