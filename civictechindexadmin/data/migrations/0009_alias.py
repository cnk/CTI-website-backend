# Generated by Django 3.1.5 on 2021-02-05 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_add_link_status_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('alias', models.CharField(max_length=30)),
            ],
        ),
    ]