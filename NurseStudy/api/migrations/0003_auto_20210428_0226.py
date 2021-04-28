# Generated by Django 3.1.7 on 2021-04-28 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210428_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='methodology',
            name='methodology',
            field=models.CharField(choices=[('CEFALOCAUDAL', 'Cefalocaudal'), ('HABITOS', 'Hábitos Externos'), ('PATRONES', 'Por Patrones Funcionales'), ('ANAMNESIS', 'Anamnésis de enfermería'), ('PALPACION', 'Palpación'), ('INSPECCION', 'Inspección')], default='CEFALOCAUDAL', max_length=255),
        ),
    ]
