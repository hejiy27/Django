# Generated by Django 2.2.3 on 2019-08-05 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_auto_20190805_0145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name': '패스트캠퍼스 사용자', 'verbose_name_plural': '패스트캠퍼스 사용자'},
        ),
    ]