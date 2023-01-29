# Generated by Django 4.1.2 on 2023-01-17 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lacrosse_app', '0006_stick_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shots', to='lacrosse_app.player')),
            ],
        ),
    ]