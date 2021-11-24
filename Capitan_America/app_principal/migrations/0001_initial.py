# Generated by Django 3.1 on 2020-08-30 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona_Salvada',
            fields=[
                ('id_persona', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_persona_salvada', models.CharField(max_length=30)),
                ('edad_persona_salvada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('dni_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres_usuario', models.CharField(max_length=30)),
                ('apellidos_usuario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Enemigo',
            fields=[
                ('alias_enemigo', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre_real_enemigo', models.CharField(max_length=30)),
                ('habilidad_principal_enemigo', models.CharField(max_length=20)),
                ('es_extraterrestre_enemigo', models.BooleanField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_principal.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('ref_contrato', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_patrocinador', models.CharField(max_length=30)),
                ('inicio_contrato', models.DateField()),
                ('fin_contrato', models.DateField()),
                ('ganancia_por_contrato', models.FloatField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_principal.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Companero_Equipo',
            fields=[
                ('nombre_companero', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('telefono_companero', models.CharField(max_length=15)),
                ('email_companero', models.EmailField(max_length=254)),
                ('cumpleanos_companero', models.DateField(blank=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_principal.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Aliado',
            fields=[
                ('nombre_aliado', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('idioma_aliado', models.CharField(max_length=20)),
                ('es_extraterrestre_aliado', models.BooleanField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_principal.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Mision',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre_mision', models.CharField(max_length=20, unique=True)),
                ('fecha', models.DateTimeField(unique=True)),
                ('pendiente', models.BooleanField(default=False)),
                ('cumplida', models.BooleanField(default=False)),
                ('fallida', models.BooleanField(default=False)),
                ('observaciones', models.TextField(blank=True, max_length=400)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_principal.usuario')),
            ],
            options={
                'unique_together': {('usuario', 'codigo')},
            },
        ),
        migrations.CreateModel(
            name='Hecho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar_hecho', models.CharField(max_length=20)),
                ('fecha_hecho', models.DateField()),
                ('descripcion_hecho', models.TextField(blank=True, max_length=400)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_principal.persona_salvada')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_principal.usuario')),
            ],
            options={
                'unique_together': {('persona', 'fecha_hecho', 'lugar_hecho')},
            },
        ),
    ]