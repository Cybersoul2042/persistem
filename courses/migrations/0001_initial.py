# Generated by Django 5.0.7 on 2024-07-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('published', models.DateTimeField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='')),
                ('doc', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('mr1', models.CharField(max_length=50)),
                ('mr2', models.CharField(blank=True, max_length=50)),
                ('mr3', models.CharField(blank=True, max_length=50)),
                ('mr4', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
