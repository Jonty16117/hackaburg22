# Generated by Django 4.0.6 on 2022-07-08 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('room_capacity', models.IntegerField()),
                ('energy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_parking', models.IntegerField()),
                ('date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.usersmodel')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeBookingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.usersmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FoodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.usersmodel')),
            ],
        ),
        migrations.CreateModel(
            name='DailyRoomBookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.roomsmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.usersmodel')),
            ],
        ),
    ]
