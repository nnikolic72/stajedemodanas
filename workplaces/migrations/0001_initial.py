# Generated by Django 2.1 on 2018-08-19 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('receivers', '0001_initial'),
        ('deliverers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiverGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_group_name', models.CharField(max_length=50, verbose_name='Group Name')),
                ('receiver_group_office', models.CharField(blank=True, max_length=50, null=True, verbose_name='Office # and Floor #')),
            ],
            options={
                'verbose_name': 'Receiver Group',
                'verbose_name_plural': 'Receiver Groups',
            },
        ),
        migrations.CreateModel(
            name='ReceiverGroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_money_person', models.BooleanField(default=False, verbose_name='Is Collecting Money')),
                ('is_money_person_deputy', models.BooleanField(default=False, verbose_name='Is Collecting Money (Deputy)')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receivers.Receiver')),
                ('receiver_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workplaces.ReceiverGroup')),
            ],
            options={
                'verbose_name': 'Receiver Group Member',
                'verbose_name_plural': 'Receiver Group Members',
            },
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace_name', models.CharField(max_length=120)),
                ('workplace_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliverers.Address')),
            ],
            options={
                'verbose_name': 'Workplace',
                'verbose_name_plural': 'Workplaces',
            },
        ),
    ]