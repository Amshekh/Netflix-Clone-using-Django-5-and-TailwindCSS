# Generated by Django 5.0 on 2023-12-23 14:01

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_netflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profiles',
            field=models.ManyToManyField(to='app_netflix.profile'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(blank=True, choices=[('All', 'All'), ('Kids', 'Kids')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='flyer',
            field=models.ImageField(blank=True, null=True, upload_to='flyers'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.CharField(choices=[('single', 'Single'), ('seasonal', 'Seasonal')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
