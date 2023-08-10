# Generated by Django 4.2 on 2023-07-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='photos/img')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=30)),
            ],
        ),
    ]
