# Generated by Django 3.2.13 on 2022-06-26 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_userprofile_blood_type'),
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('modifiedAt', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETE', 'Complete'), ('CANCELED', 'Canceled')], max_length=8)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='users.userprofile')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='requests.request')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
