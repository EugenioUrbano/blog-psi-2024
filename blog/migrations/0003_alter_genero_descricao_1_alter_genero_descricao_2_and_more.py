# Generated by Django 5.1 on 2024-09-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_genero_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='descricao_1',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='genero',
            name='descricao_2',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='genero',
            name='descricao_3',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='genero',
            name='descricao_4',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='genero',
            name='descricao_5',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='genero',
            name='descricao_6',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='genero',
            name='descricao_7',
            field=models.TextField(max_length=600),
        ),
    ]
