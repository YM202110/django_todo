# Generated by Django 3.2.8 on 2021-12-28 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='タスク名')),
                ('description', models.TextField(blank=True, verbose_name='詳細')),
                ('deadline', models.DateField(verbose_name='締切')),
            ],
        ),
    ]
