# Generated by Django 4.2 on 2024-04-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_alter_service_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='ecitizen',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='service',
            name='enhancement',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Digital', 'Digital')], max_length=20),
        ),
    ]
