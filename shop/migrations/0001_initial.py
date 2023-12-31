# Generated by Django 4.2.2 on 2023-07-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
