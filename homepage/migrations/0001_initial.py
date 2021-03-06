# Generated by Django 3.2.11 on 2022-04-22 13:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('content', models.FileField(blank=True, default=None, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('publication_date', models.IntegerField(default='2022', validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(1900)])),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('POSTED', 'Posted'), ('DELETED', 'Deleted')], max_length=10, null=True)),
                ('author', models.ManyToManyField(related_name='contents', to='homepage.Author')),
                ('categories', models.ManyToManyField(to='homepage.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contents', models.ManyToManyField(related_name='contents', to='homepage.Content')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='publisher',
            field=models.ManyToManyField(related_name='contents', to='homepage.Publisher'),
        ),
    ]
