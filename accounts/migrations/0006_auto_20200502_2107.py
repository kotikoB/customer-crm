# Generated by Django 3.0.5 on 2020-05-02 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200502_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out door', 'Out door')], max_length=255, null=True),
        ),
    ]
