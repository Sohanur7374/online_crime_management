# Generated by Django 3.0 on 2019-12-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('Complain_id', models.AutoField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('Complain_type', models.CharField(max_length=55)),
                ('Complainant_name', models.CharField(max_length=55)),
                ('Mobile_Number', models.CharField(max_length=55)),
                ('District', models.CharField(max_length=55)),
                ('Thana', models.CharField(max_length=55)),
                ('Address', models.CharField(max_length=55)),
                ('Complain_description', models.CharField(max_length=55)),
            ],
        ),
    ]
