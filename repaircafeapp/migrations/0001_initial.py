# Generated by Django 3.2.7 on 2021-10-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=25)),
                ('firstname_text', models.CharField(max_length=25)),
                ('email_text', models.CharField(max_length=40)),
                ('phone_text', models.CharField(max_length=14)),
                ('locality_text', models.CharField(max_length=50)),
                ('category_text', models.CharField(max_length=16)),
                ('object_text', models.CharField(max_length=50)),
                ('brand_text', models.CharField(max_length=10)),
                ('model_text', models.CharField(max_length=15)),
                ('year_text', models.CharField(max_length=4)),
                ('problem_text', models.CharField(max_length=2048)),
                ('research_text', models.CharField(max_length=2048)),
                ('actions_text', models.CharField(max_length=2048)),
                ('expectation_text', models.CharField(max_length=2048)),
                ('commitment_text', models.CharField(max_length=2048)),
                ('reparation_day_text', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]