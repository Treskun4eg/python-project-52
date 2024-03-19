# Generated by Django 4.2.11 on 2024-03-19 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
        ('tasks', '0004_alter_tasksmodel_label_alter_tasksmodel_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasksmodel',
            old_name='label',
            new_name='labels',
        ),
        migrations.AlterField(
            model_name='tasksmodel',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='statuses.statusesmodel', verbose_name='Status'),
        ),
    ]
