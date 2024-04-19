# Generated by Django 5.0.4 on 2024-04-19 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='categoria',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='descricao',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nome',
            new_name='name',
        ),
    ]
