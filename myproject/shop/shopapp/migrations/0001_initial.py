# Generated by Django 3.2.18 on 2023-04-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VipInfodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('cemail', models.EmailField(max_length=50)),
                ('cpasswd', models.CharField(max_length=50)),
                ('cphone', models.CharField(max_length=50)),
                ('cBirthday', models.DateField(null=True)),
                ('cAddr', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
