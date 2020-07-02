# Generated by Django 2.2.7 on 2020-07-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0039_auto_20200702_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amount_received',
            name='remaining_amount2',
        ),
        migrations.AlterField(
            model_name='workers',
            name='type_of_person',
            field=models.CharField(choices=[('سواق', 'سواق'), ('عامل', 'عامل'), ('إداري', 'إدارى'), ('محاسب', 'محاسب'), ('صنايعي', 'صنايعي')], default='عامل', max_length=50, verbose_name='نوع العامل'),
        ),
    ]
