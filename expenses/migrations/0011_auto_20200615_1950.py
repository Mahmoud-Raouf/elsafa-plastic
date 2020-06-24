# Generated by Django 2.2.7 on 2020-06-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0010_auto_20200615_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='type_of_person',
            field=models.CharField(choices=[('صنايعي', 'صنايعي'), ('سواق', 'سواق'), ('محاسب', 'محاسب'), ('عامل', 'عامل'), ('إداري', 'إدارى')], default='عامل', max_length=50, verbose_name='نوع العامل'),
        ),
    ]
