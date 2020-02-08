# Generated by Django 3.0.2 on 2020-01-29 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'پرداخت نشده'), (2, 'پرداخت شده'), (3, 'آماده ارسال'), (4, 'ارسال شده')], default=1)),
                ('date', models.DateTimeField(auto_now=True)),
                ('foods', models.ManyToManyField(to='foods.Foods')),
            ],
        ),
    ]
