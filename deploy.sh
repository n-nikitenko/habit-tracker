/etc/poetry/bin/poetry shell
/etc/poetry/bin/poetry  install --no-root
python3 manage.py migrate
python3 manage.py collectstatic --no-input
exit