# Generated by Django 2.0.13 on 2019-04-15 13:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happy_recite_word', '0002_excelstatus_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelstatus',
            name='pdf_file',
            field=models.FileField(null=True, upload_to='pdfs/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]