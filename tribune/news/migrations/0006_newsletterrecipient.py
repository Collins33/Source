# Generated by Django 2.0 on 2018-01-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180104_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
