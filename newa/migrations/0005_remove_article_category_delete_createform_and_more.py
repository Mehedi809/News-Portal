# Generated by Django 4.2.2 on 2023-08-08 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newa', '0004_createform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.DeleteModel(
            name='CreateForm',
        ),
        migrations.RemoveField(
            model_name='islam',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sports',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newa.category'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Islam',
        ),
        migrations.DeleteModel(
            name='Sports',
        ),
    ]
