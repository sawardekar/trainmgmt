# Generated by Django 3.2.20 on 2023-08-09 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compartment',
            fields=[
                ('comp_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=120)),
                ('schedule_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SeatAvabilty',
            fields=[
                ('seat_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('seat_no', models.IntegerField()),
                ('status', models.CharField(choices=[('Reserved', 'Reserved'), ('Open', 'Open'), ('Waiting', 'Waiting')], max_length=50)),
                ('user_name', models.CharField(max_length=200)),
                ('user_pencard', models.CharField(max_length=15)),
                ('user_mobile', models.IntegerField()),
                ('comp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_app.compartment')),
                ('train_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_app.train')),
            ],
        ),
    ]
