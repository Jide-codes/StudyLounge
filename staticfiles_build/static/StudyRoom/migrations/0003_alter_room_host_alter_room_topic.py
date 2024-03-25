# Generated by Django 4.0.4 on 2024-03-06 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyRoom', '0002_topic_room_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudyRoom.topic'),
        ),
    ]
