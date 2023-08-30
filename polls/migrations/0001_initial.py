# Generated by Django 4.2.4 on 2023-08-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='oqituvchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(default='', max_length=215)),
                ('tel_nomer', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Oquv_markaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=220)),
                ('xonalar_soni', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]