# Generated by Django 5.1 on 2024-08-25 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_student_noofdoubts_student_noofsolutions_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
    ]
