# Generated by Django 3.2.13 on 2023-09-20 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDoPedro', '0007_auto_20230920_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top1', models.CharField(max_length=50)),
                ('top2', models.CharField(max_length=50)),
                ('top3', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('comentarios', models.CharField(max_length=200)),
            ],
        ),
    ]
