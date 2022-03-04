# Generated by Django 4.0.1 on 2022-01-30 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('periods', '0002_rename_periods_period'),
        ('days', '0001_initial'),
        ('subjects', '0002_rename_subjects_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='days.day')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='periods.period')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject')),
            ],
            options={
                'unique_together': {('day', 'period', 'day')},
            },
        ),
    ]