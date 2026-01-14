@echo off
echo Starting Celery Worker with -P solo to fix Windows PermissionError...
venv\Scripts\celery -A load_test_proj worker -l info -P solo
pause
