# Generated by Django 4.2 on 2023-04-19 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyctlg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourfirm',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='companyctlg.company'),
        ),
    ]