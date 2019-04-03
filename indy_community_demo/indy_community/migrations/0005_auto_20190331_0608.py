# Generated by Django 2.0.9 on 2018-11-08 00:18

from django.db import migrations

from ..models import USER_ROLES


def create_user_roles(apps, schema_editor):
    # Creates the Atria Calendar user roles as Groups
    Group = apps.get_model('auth', 'Group')

    for role in USER_ROLES:
        Group.objects.create(name=role)

def delete_user_roles(apps, schema_editor):
    # Deletes the Atria Calendar user roles as Groups (for reverse migrations)
    Group = apps.get_model('auth', 'Group')
    role_groups = Group.objects.filter(name__in=USER_ROLES)

    role_groups.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('indy_community', '0004_auto_20190328_0248'),
    ]

    operations = [
        migrations.RunPython(create_user_roles, delete_user_roles),
    ]