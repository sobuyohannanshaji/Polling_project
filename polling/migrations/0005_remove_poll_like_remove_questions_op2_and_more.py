# Generated by Django 4.1.5 on 2023-01-18 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0004_poll_questions_op1_questions_op2_questions_op3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='like',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='op2',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='op3',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='op4',
        ),
        migrations.AddField(
            model_name='poll',
            name='op1',
            field=models.CharField(default=True, max_length=1000),
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.CharField(default=True, max_length=1000)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polling.register')),
                ('op1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polling.poll')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polling.questions')),
            ],
        ),
    ]
