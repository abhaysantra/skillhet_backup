# Generated by Django 2.2.3 on 2019-09-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillhet', '0003_sociallink'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default=None, max_length=256)),
                ('landline', models.CharField(default=None, max_length=256)),
                ('email', models.CharField(default=None, max_length=256)),
                ('web_link', models.CharField(default=None, max_length=256)),
                ('address', models.TextField(default=None)),
            ],
        ),
    ]