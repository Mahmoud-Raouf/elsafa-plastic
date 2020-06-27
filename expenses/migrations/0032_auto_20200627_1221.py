# Generated by Django 2.2.7 on 2020-06-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0031_auto_20200627_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='type_of_person',
            field=models.CharField(choices=[('محاسب', 'محاسب'), ('صنايعي', 'صنايعي'), ('عامل', 'عامل'), ('إداري', 'إدارى'), ('سواق', 'سواق')], default='عامل', max_length=50, verbose_name='نوع العامل'),
        ),
    ]
