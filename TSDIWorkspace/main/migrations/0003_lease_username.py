# Generated by Django 3.1.4 on 2021-07-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lease'),
    ]

    operations = [
        migrations.AddField(
            model_name='lease',
            name='username',
            field=models.CharField(default='tsdi', max_length=64),
            preserve_default=False,
        ),
    ]
