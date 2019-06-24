# Generated by Django 2.2 on 2019-06-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190612_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='power',
            name='suits',
            field=models.ManyToManyField(to='main_app.Suit'),
        ),
    ]
