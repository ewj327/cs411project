# Generated by Django 4.1.4 on 2022-12-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GMapDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('hours', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('price_level', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=200)),
                ('ratings_num', models.CharField(max_length=200)),
                ('query_place_id', models.CharField(max_length=200)),
                ('food_style', models.CharField(max_length=200)),
                ('food_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('avg_rating', models.CharField(max_length=200)),
                ('avg_ratings_num', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='YelpDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('price_level', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=200)),
                ('ratings_num', models.CharField(max_length=200)),
            ],
        ),
    ]
