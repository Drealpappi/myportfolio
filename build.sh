set -o errexit
pip install -r requirements.txt
# run django commands
python manage.py collectstatic --no-input
python manage.py migrate