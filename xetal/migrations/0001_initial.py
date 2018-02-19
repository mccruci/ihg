# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-19 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('dfc_cod', models.AutoField(primary_key=True, serialize=False)),
                ('dfc_nome', models.CharField(max_length=100)),
                ('dfc_indirizzo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Letto',
            fields=[
                ('ltt_cod', models.AutoField(primary_key=True, serialize=False)),
                ('ltt_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Piano',
            fields=[
                ('pno_cod', models.AutoField(primary_key=True, serialize=False)),
                ('pno_numero', models.IntegerField()),
                ('pno_dfc_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xetal.Edificio')),
            ],
        ),
        migrations.CreateModel(
            name='Reparto',
            fields=[
                ('rpt_cod', models.AutoField(primary_key=True, serialize=False)),
                ('rpt_nome', models.CharField(max_length=100)),
                ('rpt_spd_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xetal.Piano')),
            ],
        ),
        migrations.CreateModel(
            name='Sito',
            fields=[
                ('sit_cod', models.AutoField(primary_key=True, serialize=False)),
                ('sit_denominazione', models.CharField(max_length=100)),
                ('sit_ospedale', models.CharField(max_length=100)),
                ('sit_indirizzo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stanza',
            fields=[
                ('stz_cod', models.AutoField(primary_key=True, serialize=False)),
                ('stz_numero', models.IntegerField()),
                ('stz_uso', models.CharField(choices=[('D', 'Degenza'), ('C', 'Controllo')], max_length=1)),
                ('stz_pno_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xetal.Piano')),
                ('stz_rpt_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xetal.Reparto')),
            ],
        ),
        migrations.AddField(
            model_name='letto',
            name='ltt_stz_cod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xetal.Stanza'),
        ),
        migrations.AddField(
            model_name='edificio',
            name='dfc_sit_cod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xetal.Sito'),
        ),
    ]
