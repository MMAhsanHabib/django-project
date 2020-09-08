# Generated by Django 3.1 on 2020-09-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myskill', '0002_auto_20200827_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/')),
            ],
        ),
    ]
