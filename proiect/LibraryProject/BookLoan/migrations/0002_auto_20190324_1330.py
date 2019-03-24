# Generated by Django 2.1.7 on 2019-03-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookLoan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookloan',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('O', 'Open'), ('C', 'Closed')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='bookloan',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]