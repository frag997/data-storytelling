# Generated by Django 2.2.6 on 2019-10-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_votacao', models.IntegerField()),
                ('timestamp', models.CharField(max_length=30)),
                ('sigla_tipo', models.CharField(max_length=30)),
                ('numero', models.CharField(max_length=30)),
                ('ano', models.IntegerField()),
                ('obj_votacao', models.CharField(max_length=1000)),
                ('url_inteiro_teor', models.CharField(max_length=100)),
                ('id_deputado', models.CharField(max_length=30)),
                ('nome', models.CharField(max_length=100)),
                ('sigla_partido', models.CharField(max_length=30)),
                ('uf', models.CharField(max_length=30)),
                ('voto', models.CharField(max_length=30)),
                ('orient_part', models.CharField(max_length=30)),
                ('orient_gov', models.CharField(max_length=30)),
            ],
        ),
    ]
