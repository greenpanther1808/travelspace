# Generated by Django 4.1.2 on 2022-11-07 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='struct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('images', models.ImageField(upload_to='pics')),
                ('descr', models.TextField()),
            ],
        ),
    ]
