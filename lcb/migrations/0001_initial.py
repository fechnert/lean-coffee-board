# Generated by Django 3.1.7 on 2021-04-12 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('phase', models.CharField(choices=[('t', 'Think'), ('e', 'Explain'), ('v', 'Vote'), ('d', 'Discuss')], default='t', max_length=1)),
                ('title', models.CharField(max_length=512)),
                ('vote_limit', models.PositiveSmallIntegerField(default=3)),
                ('think_time_limit', models.DurationField()),
                ('discuss_time_limit', models.DurationField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lane',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position', models.PositiveSmallIntegerField(blank=True)),
                ('type', models.CharField(choices=[('g', 'Gather'), ('d', 'Discuss')], default='g', max_length=1)),
                ('title', models.CharField(max_length=512)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcb.board')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position', models.PositiveSmallIntegerField(blank=True)),
                ('title', models.CharField(max_length=512)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcb.board')),
                ('lane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcb.lane')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards_created', to=settings.AUTH_USER_MODEL)),
                ('votes', models.ManyToManyField(blank=True, related_name='cards_voted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
