from django.db import migrations


def install_unaccent(apps, schema_editor):
    if schema_editor.connection.vendor == 'postgresql':
        schema_editor.execute('CREATE EXTENSION IF NOT EXISTS unaccent;')


def uninstall_unaccent(apps, schema_editor):
    if schema_editor.connection.vendor == 'postgresql':
        schema_editor.execute('DROP EXTENSION IF EXISTS unaccent;')


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0010_remove_inventario_imagen_rota_and_more'),
    ]

    operations = [
        migrations.RunPython(install_unaccent, reverse_code=uninstall_unaccent),
    ]
