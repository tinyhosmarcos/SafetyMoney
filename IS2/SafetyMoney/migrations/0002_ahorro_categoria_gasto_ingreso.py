# Generated by Django 2.2.7 on 2020-06-01 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SafetyMoney', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ahorro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('monto_objetivo', models.DecimalField(decimal_places=4, max_digits=10)),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SafetyMoney.Grupo')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SafetyMoney.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('periodo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=4, max_digits=10)),
                ('descripcion', models.CharField(max_length=30)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('ahorro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SafetyMoney.Ahorro')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SafetyMoney.Categoria')),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SafetyMoney.Grupo')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SafetyMoney.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=4, max_digits=10)),
                ('descripcion', models.CharField(max_length=30)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SafetyMoney.Categoria')),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SafetyMoney.Grupo')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SafetyMoney.Usuario')),
            ],
        ),
    ]
