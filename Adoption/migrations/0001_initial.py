# Generated by Django 3.2.7 on 2021-09-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage1', models.ImageField(upload_to='Adoption')),
                ('name', models.CharField(max_length=264)),
            ],
        ),
    ]
