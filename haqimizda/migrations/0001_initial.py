# Generated by Django 4.0.3 on 2022-03-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ishtirokchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True)),
                ('rasm', models.ImageField(upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]