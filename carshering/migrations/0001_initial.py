# Generated by Django 3.1.1 on 2020-09-13 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sharing_images/', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда',
                'verbose_name_plural': 'Звезды',
            },
        ),
        migrations.CreateModel(
            name='Sharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('companyname', models.CharField(max_length=150, verbose_name='Название')),
                ('places', models.SmallIntegerField(default=0, verbose_name='Количество мест')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('goodprices', models.CharField(default='Км', max_length=120, verbose_name='За:')),
                ('sitelink', models.CharField(default=None, max_length=220, verbose_name='Ссылка на сайт')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('images', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='carshering.image')),
                ('safetystar', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='carshering.star', verbose_name='Звезда безопасности')),
            ],
        ),
    ]
