# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affairs',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('type', models.SmallIntegerField()),
                ('place', models.CharField(default='未填写', max_length=30)),
                ('details', models.CharField(default='无', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('introduction', models.CharField(default='无', max_length=100)),
                ('establish_date', models.DateField(auto_now=True)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('is_public', models.BooleanField()),
                ('max_member', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Group_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privilege', models.SmallIntegerField()),
                ('visible', models.BooleanField(default=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.Group')),
            ],
        ),
        migrations.CreateModel(
            name='HaveAffair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affair_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.Affairs')),
            ],
        ),
        migrations.CreateModel(
            name='InGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.Group')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.Group_User')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SingleAffairsTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField()),
                ('affair_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.Affairs')),
            ],
        ),
        migrations.CreateModel(
            name='SuccessiveAffairsTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('startData', models.DateField()),
                ('lastData', models.DateField()),
                ('every', models.SmallIntegerField()),
                ('affair_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.Affairs')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=64)),
                ('stu_id', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=15)),
                ('realname', models.CharField(max_length=10, null=True)),
                ('gender', models.SmallIntegerField()),
                ('birthday', models.DateField(null=True)),
                ('mobile', models.CharField(max_length=21)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('updatetime', models.DateField(auto_now_add=True)),
                ('major', models.CharField(max_length=30)),
                ('entry_date', models.DateField()),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.School')),
            ],
        ),
        migrations.AddField(
            model_name='ingroup',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.User'),
        ),
        migrations.AddField(
            model_name='haveaffair',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.User'),
        ),
        migrations.AddField(
            model_name='group_user',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.User'),
        ),
        migrations.AddField(
            model_name='affairs',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resource.User'),
        ),
    ]