# Generated by Django 2.0.13 on 2019-04-18 18:36

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='EXCEL 名称')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('xl_file', models.FileField(upload_to='%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['xlsx', 'csv'])], verbose_name='EXCEL 文件')),
                ('recite_time', models.DateTimeField(default=datetime.datetime(2000, 1, 1, 1, 1, 1, 1), verbose_name='背诵日期')),
                ('pdf_file', models.FileField(default='None', help_text='单词本', upload_to='pdfs/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('ans_file', models.FileField(default='None', help_text='答案本', upload_to='pdfs/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en', models.CharField(default=' ', help_text='en : 请在此输入英文', max_length=400, verbose_name='英语')),
                ('cn', models.CharField(default=' ', help_text='cn : 请在此输入中文', max_length=400, verbose_name='中文')),
                ('comment', models.TextField(default=' ', help_text='comment : 请在此输入备注', max_length=255, verbose_name='备注')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('recite_time', models.DateTimeField(default=datetime.datetime(2000, 1, 1, 1, 1, 1, 1), verbose_name='背诵日期')),
                ('recite_count', models.IntegerField(default=0, verbose_name='背诵次数')),
                ('cn2en', models.SmallIntegerField(choices=[(1, 'CN2EN'), (2, 'EN2CN'), (0, 'ALL ALLOW')], default=0, help_text='cn2en : 1 代表中翻英，2代表英翻中，0（默认）代表都可以，系统会取随机数', verbose_name='中翻英')),
                ('word_or_sentence', models.SmallIntegerField(choices=[(1, 'Word'), (2, 'Sentence')], default=1, help_text='WorS(word_or_sentence) : 1(默认) 代表单词; 2 代表句子', verbose_name='单词还是句子')),
                ('enshrine_time', models.IntegerField(default=0, help_text='收藏一次单词,该数量自增1', verbose_name='收藏次数')),
                ('file_source', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='source', to='happy_recite_word.ExcelStatus', verbose_name='所属EXCEL文件')),
            ],
        ),
    ]
