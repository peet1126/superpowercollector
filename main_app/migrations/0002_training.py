# Generated by Django 2.2 on 2019-06-12 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('practice', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('E', 'Evening')], default='M', max_length=1)),
                ('power', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Power')),
            ],
        ),
    ]
