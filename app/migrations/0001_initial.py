# Generated by Django 4.2.6 on 2023-12-06 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('sport', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.players')),
            ],
        ),
        migrations.CreateModel(
            name='AccessRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
    ]
