# Generated by Django 5.0.6 on 2024-08-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_rename_bank_loanenquiry_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanenquiry',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=100, null=True),
        ),
    ]
