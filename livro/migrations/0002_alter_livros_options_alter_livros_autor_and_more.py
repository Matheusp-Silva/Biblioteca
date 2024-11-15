# Generated by Django 5.0.9 on 2024-11-01 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livros',
            options={'verbose_name': 'Livro'},
        ),
        migrations.AlterField(
            model_name='livros',
            name='autor',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='livros',
            name='co_autor',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 1, 17, 7, 26, 916799)),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_devolucao',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_emprestimo',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='nome_emprestado',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='livros',
            name='tempo_duracao',
            field=models.DateTimeField(blank=True),
        ),
    ]
