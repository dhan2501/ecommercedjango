# Generated by Django 5.0 on 2024-01-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='uploads/products/'),
        ),
    ]
