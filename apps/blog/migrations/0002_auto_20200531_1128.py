# Generated by Django 3.0.6 on 2020-05-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uuid',
            field=models.CharField(editable=False, max_length=255, primary_key=True, serialize=False),
        ),
    ]