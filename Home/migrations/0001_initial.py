# Generated by Django 4.0.3 on 2022-03-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrontSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/slider-img')),
                ('discount_deal', models.CharField(choices=[('Hot Deals', 'Hot Deals'), ('New Arraivals', 'New Arraivals')], max_length=100)),
                ('Sale', models.IntegerField()),
                ('brand_name', models.CharField(max_length=200)),
                ('discount', models.IntegerField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
