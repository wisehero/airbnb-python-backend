# Generated by Django 4.1 on 2022-10-23 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='kind',
            field=models.CharField(choices=[('rooms', 'Rooms'), ('experiences', 'Experiences')], max_length=150),
        ),
    ]