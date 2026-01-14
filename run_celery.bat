@echo off
echo Starting Celery Worker with -P threads for concurrency...
venv\Scripts\celery -A load_test_proj worker -l info -P threads -c 10
pause
