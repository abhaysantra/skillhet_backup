# Generated by Django 2.2.3 on 2019-09-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillhet', '0012_auto_20190926_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteaddress',
            name='footer_content',
            field=models.TextField(default=None),
        ),
    ]
