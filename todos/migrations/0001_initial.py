# Generated by Django 5.1.4 on 2024-12-10 22:41

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
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('finished_at', models.DateField(null=True)),
            ],
        ),
    ]
