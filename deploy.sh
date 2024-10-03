/etc/poetry/bin/poetry shell
/etc/poetry/bin/poetry  install --no-root
/etc/poetry/bin/poetry run pip3 install gunicorn
/etc/poetry/bin/poetry run python3 manage.py migrate
/etc/poetry/bin/poetry run python3 manage.py collectstatic --no-input
exit