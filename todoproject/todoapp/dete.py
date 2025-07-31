import sys
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')
django.setup()

from todoapp.models import Task
from django.utils.timezone import now

def backfill_created_updated():
    tasks_without_created = Task.objects.filter(created_at__isnull=True)
    count = tasks_without_created.count()

    for task in tasks_without_created:
        task.created_at = now()  # Or customize logic here
        # If you also have an updated_at field, update it as well
        if hasattr(task, 'updated_at'):
            task.updated_at = now()
        task.save()

    print(f"Backfilled created_at for {count} tasks.")

if __name__ == "__main__":
    backfill_created_updated()
