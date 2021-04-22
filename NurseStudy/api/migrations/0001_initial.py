# Generated by Django 3.1.7 on 2021-04-21 18:51

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(editable=False)),
                ('updated_date', models.DateTimeField(editable=False)),
                ('right_answer', models.CharField(max_length=255)),
                ('wrong_answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=255), size=10)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataAcquisitionMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('OBSERVACION', 'Observación'), ('ENTREVISTA', 'Entrevista'), ('EXPLORACION', 'Exploración Física')], default='OBSERVACION', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Methodology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methodology', models.CharField(choices=[('CEFALOCAUDAL', 'Cefalocaudal'), ('HABITOS', 'Hábitos Externos'), ('PATRONES', 'Por Patrones Funcionales'), ('ANAMNESIS', 'Anamnésis de enfermería'), ('AUSCULTACION', 'Auscultación'), ('PALPACION', 'Palpación'), ('PERCUSION', 'Percursión'), ('INSPECCION', 'Inspección')], default='CEFALOCAUDAL', max_length=255)),
                ('data_acquisition_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='methodologies', to='api.dataacquisitionmethod')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(editable=False)),
                ('updated_date', models.DateTimeField(editable=False)),
                ('question', models.CharField(max_length=255)),
                ('difficulty', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('question_type', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)])),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255)),
                ('answer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='question', to='api.answer')),
                ('methodology', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='api.methodology')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methodology_progress', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(18)])),
                ('methodology', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='progresses', to='api.methodology')),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_answer', models.CharField(max_length=255)),
                ('result', models.BooleanField()),
                ('created_by', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='grades', to='api.question')),
            ],
        ),
    ]
