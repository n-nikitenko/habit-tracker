~/.local/share/pypoetry/venv/bin/poetry shell
~/.local/share/pypoetry/venv/bin/poetry  install --no-root
python3 manage.py migrate
python3 manage.py collectstatic --no-input
exit