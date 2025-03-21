# Generated by Django 5.1.4 on 2024-12-21 04:20

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('descricao_item', models.TextField(blank=True, null=True)),
                ('categoria', models.CharField(choices=[('Livro', 'Livro'), ('Jogo', 'Jogo'), ('Filme/Série', 'Filme Ou Serie'), ('Action Figure', 'Action Figure')], default='Livro', max_length=50)),
                ('ano_aquisicao', models.IntegerField(help_text='Informe o ano da aquisição do item (ex.: 2018)', validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2024)])),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
