# Generated by Django 4.0.4 on 2022-04-28 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('L', 'Large'), ('M', 'Medium'), ('S', 'Small')], default='L', max_length=1, verbose_name='Lace Size')),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='buyer',
            options={'ordering': ['-bought']},
        ),
        migrations.AlterField(
            model_name='buyer',
            name='bought',
            field=models.DateField(verbose_name='Date Bought'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Buyer Name'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='size',
            field=models.CharField(choices=[('11', 'Size 11'), ('10', 'Size 10'), ('9', 'Size 9'), ('8', 'Size 8'), ('7', 'Size 7')], default='11', max_length=2, verbose_name='Size Bought'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='value',
            field=models.IntegerField(verbose_name='Resell Price'),
        ),
        migrations.AlterField(
            model_name='sneaker',
            name='price',
            field=models.IntegerField(verbose_name='Retail Price'),
        ),
    ]
