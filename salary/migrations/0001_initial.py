# Generated by Django 2.2.7 on 2020-06-14 08:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import salary.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_auto_20200614_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=salary.models.random_string, verbose_name='كود المنتج')),
                ('description', models.CharField(max_length=50, verbose_name='وصف المنتج')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاريخ الإضافة')),
                ('price', models.IntegerField(verbose_name='سعر المنتج')),
                ('count', models.FloatField(verbose_name='الكمية')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nameofproduct', to='products.Product', verbose_name='إسم المنتج')),
                ('typeofproducts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='typeofproducts')),
            ],
            options={
                'verbose_name': 'Salary',
                'verbose_name_plural': 'Salarys',
            },
        ),
    ]
