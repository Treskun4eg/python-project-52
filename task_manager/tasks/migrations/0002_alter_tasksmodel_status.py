# Generated by Django 4.2.10 on 2024-02-27 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0003_rename_name_statusesmodel_status'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksmodel',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='statuses.statusesmodel', verbose_name='Status'),
        ),
    ]
