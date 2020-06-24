# Generated by Django 2.2.7 on 2020-06-15 09:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_auto_20200614_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='عنوان الصيانة')),
                ('description', models.TextField(verbose_name='وصف الصيانة')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاريخ الإضافة')),
                ('cost', models.FloatField(verbose_name='تكلفة الصيانه')),
            ],
            options={
                'verbose_name': 'Servicing',
                'verbose_name_plural': 'Servicings',
            },
        ),
        migrations.RemoveField(
            model_name='workers',
            name='Salary_discounts',
        ),
        migrations.AlterField(
            model_name='workers',
            name='type_of_person',
            field=models.CharField(choices=[('سواق', 'سواق'), ('صنايعي', 'صنايعي'), ('محاسب', 'محاسب'), ('إداري', 'إدارى'), ('عامل', 'عامل')], default='عامل', max_length=50, verbose_name='نوع العامل'),
        ),
    ]
