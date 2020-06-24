# Generated by Django 2.2.7 on 2020-06-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20200622_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmix',
            name='price1',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامة فى الخلطة'),
        ),
        migrations.AddField(
            model_name='productmix',
            name='price2',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامة فى الخلطة'),
        ),
        migrations.AddField(
            model_name='productmix',
            name='price3',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامة فى الخلطة'),
        ),
        migrations.AddField(
            model_name='productmix',
            name='price4',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامة فى الخلطة'),
        ),
        migrations.AddField(
            model_name='productmix',
            name='price5',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامة فى الخلطة'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type1',
            field=models.CharField(choices=[('الأوميالين', 'الأوميالين'), ('تخريز', 'تخريز'), ('الصبغة ', 'الصبغة '), ('ريسايكل', 'ريسايكل'), ('بولى اثلين', 'بولى اثلين')], max_length=50, verbose_name='إسم الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type1_count',
            field=models.FloatField(blank=True, null=True, verbose_name='نسبة الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type1_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type2',
            field=models.CharField(choices=[('الأوميالين', 'الأوميالين'), ('تخريز', 'تخريز'), ('الصبغة ', 'الصبغة '), ('ريسايكل', 'ريسايكل'), ('بولى اثلين', 'بولى اثلين')], max_length=50, verbose_name='إسم الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type2_count',
            field=models.FloatField(blank=True, null=True, verbose_name='نسبة الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type2_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type3',
            field=models.CharField(choices=[('الأوميالين', 'الأوميالين'), ('تخريز', 'تخريز'), ('الصبغة ', 'الصبغة '), ('ريسايكل', 'ريسايكل'), ('بولى اثلين', 'بولى اثلين')], max_length=50, verbose_name='إسم الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type3_count',
            field=models.FloatField(blank=True, null=True, verbose_name='نسبة الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type3_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type4',
            field=models.CharField(choices=[('الأوميالين', 'الأوميالين'), ('تخريز', 'تخريز'), ('الصبغة ', 'الصبغة '), ('ريسايكل', 'ريسايكل'), ('بولى اثلين', 'بولى اثلين')], max_length=50, verbose_name='إسم الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type4_count',
            field=models.FloatField(blank=True, null=True, verbose_name='نسبة الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type4_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type5',
            field=models.CharField(choices=[('الأوميالين', 'الأوميالين'), ('تخريز', 'تخريز'), ('الصبغة ', 'الصبغة '), ('ريسايكل', 'ريسايكل'), ('بولى اثلين', 'بولى اثلين')], max_length=50, verbose_name='إسم الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type5_count',
            field=models.FloatField(blank=True, null=True, verbose_name='نسبة الخامه'),
        ),
        migrations.AlterField(
            model_name='productmix',
            name='type5_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الخامه'),
        ),
    ]
