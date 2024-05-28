# Generated by Django 5.0.6 on 2024-05-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Desc', models.CharField(max_length=250)),
                ('Img', models.ImageField(upload_to='images/')),
                ('Ammt', models.IntegerField()),
            ],
            options={
                'db_table': 'Form',
            },
        ),
    ]
