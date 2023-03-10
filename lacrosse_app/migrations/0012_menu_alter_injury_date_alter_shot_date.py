# Generated by Django 4.1.2 on 2023-01-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lacrosse_app', '0011_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('image', models.ImageField(upload_to='images')),
                ('content', models.TextField(verbose_name='content')),
                ('date', models.TextField(verbose_name='date')),
            ],
        ),
        migrations.AlterField(
            model_name='injury',
            name='date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='shot',
            name='date',
            field=models.TextField(),
        ),
    ]
