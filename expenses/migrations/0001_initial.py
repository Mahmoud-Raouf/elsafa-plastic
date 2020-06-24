# Generated by Django 2.2.7 on 2020-06-14 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='إسم العامل')),
                ('type_of_person', models.CharField(choices=[('صنايعي', 'صنايعي'), ('محاسب', 'محاسب'), ('إداري', 'إدارى'), ('عامل', 'عامل'), ('سواق', 'سواق')], default='عامل', max_length=50, verbose_name='نوع العامل')),
                ('code', models.IntegerField(verbose_name='كود العامل')),
                ('description', models.TextField(verbose_name='وصف العامل')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاريخ الإضافة')),
                ('price', models.FloatField(verbose_name='راتب العامل ')),
                ('count', models.FloatField(verbose_name='السلف')),
            ],
            options={
                'verbose_name': 'Workers',
                'verbose_name_plural': 'Workerss',
            },
        ),
    ]
