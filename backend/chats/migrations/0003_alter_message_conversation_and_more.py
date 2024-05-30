# Generated by Django 5.0.4 on 2024-05-30 04:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_user_conversation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chats.conversation'),
        ),
        migrations.AlterField(
            model_name='message',
            name='conversation_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_messages', to='chats.user_conversation'),
        ),
    ]
