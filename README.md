# celery -A load_test_proj  worker -l info
# celery -A load_test_proj worker -l info -P solo
# python manage.py load_test --num 2000 --size 10

To run 1 task that uses 1GB of RAM:

bash
python manage.py load_test --num 1 --size 1
To run 3 tasks (totaling ~3GB RAM usage):

bash
python manage.py load_test --num 3 --size 1
