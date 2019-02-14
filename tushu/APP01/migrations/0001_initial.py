# Generated by Django 2.1.7 on 2019-02-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='出版社',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('名称', models.CharField(max_length=32, unique=True, verbose_name='名称')),
                ('地址', models.CharField(max_length=32, verbose_name='地址')),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
            },
        ),
    ]