# Generated by Django 4.2 on 2023-04-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_product_usermodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('watch', models.ManyToManyField(to='pages.video')),
            ],
        ),
    ]