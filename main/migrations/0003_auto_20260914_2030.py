from django.db import migrations
from django.core.management import call_command

def load_my_initial_data(apps, schema_editor):
    # This runs automatically during the migration
    try:
        call_command('loaddata', 'main_data.json')
    except Exception as e:
        print(f"Skipping data load or encountered error: {e}")

class Migration(migrations.Migration):

    dependencies = [
        # Leave whatever Django auto-generated here alone!
        ('main', '0001_initial'), 
    ]

    operations = [
        # Tell Django to run our custom function
        migrations.RunPython(load_my_initial_data),
    ]