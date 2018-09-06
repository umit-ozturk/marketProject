# Generated by Django 2.0.2 on 2018-09-01 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20180901_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcompany',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.Ticket', verbose_name='Ticket'),
        ),
    ]