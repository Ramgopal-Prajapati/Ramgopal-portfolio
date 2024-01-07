# Generated by Django 4.2.6 on 2023-11-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='myrevies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_imgs', models.FileField(upload_to='static/userimg')),
                ('u_name', models.CharField(max_length=30)),
                ('u_profession', models.CharField(max_length=100)),
                ('u_number', models.IntegerField(max_length=10)),
                ('u_rating', models.CharField(max_length=100)),
                ('u_feedback', models.CharField(max_length=100)),
                ('u_suggesion', models.CharField(max_length=100)),
            ],
        ),
    ]