# Generated by Django 3.2.13 on 2023-09-20 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDoPedro', '0008_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='comentarios',
        ),
        migrations.AddField(
            model_name='user',
            name='usuario_nome',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]