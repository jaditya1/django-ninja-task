# Generated by Django 4.1.3 on 2022-11-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SeedMgmt', '0002_alter_seed_options_alter_tag_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='short_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Short Name'),
        ),
    ]
