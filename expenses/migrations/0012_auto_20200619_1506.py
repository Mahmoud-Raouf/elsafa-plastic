# Generated by Django 2.2.7 on 2020-06-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0011_auto_20200615_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='type_of_person',
            field=models.CharField(choices=[('محاسب', 'محاسب'), ('صنايعي', 'صنايعي'), ('إداري', 'إدارى'), ('عامل', 'عامل'), ('سواق', 'سواق')], default='عامل', max_length=50, verbose_name='نوع العامل'),
        ),
    ]
