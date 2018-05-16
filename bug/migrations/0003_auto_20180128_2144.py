# Generated by Django 2.0 on 2018-01-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_auto_20180110_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='buglevel',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='3', max_length=200, null=True, verbose_name='严重程度'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='bugstatus',
            field=models.CharField(choices=[('激活', '激活'), ('已解决', '已解决'), ('已关闭', '已关闭')], default='激活', max_length=200, null=True, verbose_name='解决状态'),
        ),
    ]