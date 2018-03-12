# Generated by Django 2.0.3 on 2018-03-12 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmp_desc', models.CharField(max_length=20)),
                ('tmp_body', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=50)),
                ('ad_body', models.TextField()),
                ('ad_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('answer', models.TextField(choices=[('ans_this_wk', 'this_week'), ('ans_this_wk<18', 'this_week<18'), ('ans_mr_this_wk', 'mr_this_week'), ('ans_ms_this_wk', 'ms_this_week'), ('ans_next_wk', 'next_week'), ('ans_next_wk<18', 'next_week<18'), ('ans_mr_next_wk', 'mr_next_week'), ('ans_ms_next_wk', 'ms_next_week'), ('ans_other_term', 'other_term'), ('ans_other_term_mr', 'mr_other_term'), ('ans_other_term_ms', 'ms_other_term'), ('ans_office', 'office'), ('inv_m_orday', 'inv_m'), ('inv_m_wknday', 'inv_m_wknd'), ('inv_f_orday', 'inv_f'), ('inv_f_wknday', 'inv_f_wknd'), ('inv_mr_orday', 'inv_mr'), ('inv_mr_wknday', 'inv_mr_wknd'), ('inv_ms_orday', 'inv_ms'), ('inv_ms_wknday', 'inv_ms_wknd'), ('inv_scnd', 'inv_rptd'), ('inv_mr_scnd', 'inv_mr_rptd'), ('inv_ms_scnd', 'inv_ms_rptd'), ('ans_blank', 'manual')], default='ans_this_wk')),
                ('status', models.CharField(default='incoming', max_length=10)),
            ],
        ),
    ]