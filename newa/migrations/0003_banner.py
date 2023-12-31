# Generated by Django 4.2.2 on 2023-07-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newa', '0002_sports_islam_international'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='BannerImage')),
                ('http_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Banner',
            },
        ),
    ]
