# Generated by Django 3.0 on 2020-05-31 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackinfo2', '0002_userdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='branch',
            new_name='branch1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='college',
            new_name='college1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='contact',
            new_name='contact1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='email',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='firstname',
            new_name='firstname1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='gender',
            new_name='gender1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='github',
            new_name='github1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='lastname',
            new_name='lastname1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='linkedin',
            new_name='linkedin1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='pub_date',
            new_name='pub_date1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='statusid',
            new_name='statusid1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='teamname',
            new_name='teamname1',
        ),
        migrations.RenameField(
            model_name='leaderdetail',
            old_name='yearofstudy',
            new_name='yearofstudy1',
        ),
    ]