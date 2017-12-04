# Generated by Django 2.0 on 2017-12-04 00:09

import definable_serializer.models.compat
import definable_serializer.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('data', definable_serializer.models.compat.YAMLField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', definable_serializer.models.fields.DefinableSerializerByYAMLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='for_test.Paper'),
        ),
        migrations.AddField(
            model_name='answer',
            name='respondent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('paper', 'respondent')},
        ),
    ]
