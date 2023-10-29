# Generated by Django 4.2.4 on 2023-10-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0008_alter_menuitem_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='code_name',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='parent',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='position',
            field=models.PositiveIntegerField(verbose_name='Позиция пункта в меню'),
        ),
        migrations.CreateModel(
            name='CreateMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(help_text='По этому названию будет вызываться меню в коде', max_length=50, verbose_name='Кодовое название меню')),
                ('children', models.ManyToManyField(to='menus.menuitem', verbose_name='Выберите пункты данного меню')),
            ],
            options={
                'verbose_name': 'Создание меню',
            },
        ),
    ]
