# Generated by Django 4.1.5 on 2023-01-20 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0015_alter_vote_op1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='name',
        ),
    ]
