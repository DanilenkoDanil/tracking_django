# Generated by Django 4.1.5 on 2023-02-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_signal_source_signalresult_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_for_bot', models.CharField(max_length=200)),
            ],
        ),
    ]
