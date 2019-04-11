# Generated by Django 2.1.7 on 2019-03-23 14:23

import django.db.models.deletion
import jsonfallback.fields
from django.db import migrations, models

import pretix.base.models.base
import pretix.base.models.fields
import pretix.base.models.seating


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0116_auto_20190402_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190)),
                ('blocked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SeatCategoryMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layout_category', models.CharField(max_length=190)),
            ],
        ),
        migrations.CreateModel(
            name='SeatingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, verbose_name='Name')),
                ('layout', models.TextField(validators=[pretix.base.models.seating.SeatingPlanLayoutValidator()])),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seating_plans', to='pretixbase.Organizer')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, pretix.base.models.base.LoggingMixin),
        ),
        migrations.AddField(
            model_name='seatcategorymapping',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_category_mappings', to='pretixbase.Event'),
        ),
        migrations.AddField(
            model_name='seatcategorymapping',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_category_mappings', to='pretixbase.Item'),
        ),
        migrations.AddField(
            model_name='seatcategorymapping',
            name='subevent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seat_category_mappings', to='pretixbase.SubEvent'),
        ),
        migrations.AddField(
            model_name='seat',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='pretixbase.Event'),
        ),
        migrations.AddField(
            model_name='seat',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='pretixbase.Item'),
        ),
        migrations.AddField(
            model_name='seat',
            name='subevent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='pretixbase.SubEvent'),
        ),
        migrations.AddField(
            model_name='cartposition',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pretixbase.Seat'),
        ),
        migrations.AddField(
            model_name='event',
            name='seating_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='events', to='pretixbase.SeatingPlan'),
        ),
        migrations.AddField(
            model_name='orderposition',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pretixbase.Seat'),
        ),
        migrations.AddField(
            model_name='subevent',
            name='seating_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subevents', to='pretixbase.SeatingPlan'),
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_guid',
            field=models.CharField(db_index=True, default='', max_length=190),
            preserve_default=False,
        ),
    ]
