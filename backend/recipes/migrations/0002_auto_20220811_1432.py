# Generated by Django 2.2.27 on 2022-08-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_recipes/', verbose_name='Изображение'),
        ),
    ]
