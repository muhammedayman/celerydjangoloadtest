# myapp/management/commands/load_test.py
from django.core.management.base import BaseCommand
from tasks import mock_heavy_task

class Command(BaseCommand):
    help = "Enqueue Celery tasks for load testing"

    def add_arguments(self, parser):
        parser.add_argument('--num', type=int, default=100)
        parser.add_argument('--size', type=int, default=3)

    def handle(self, *args, **options):
        num = options['num']
        size = options['size']
        for i in range(num):
            mock_heavy_task.delay(size)
            self.stdout.write(self.style.SUCCESS(f"Queued task {i+1}/{num}"))