web: newrelic-admin run-program python django/manage.py run_gunicorn -b 0.0.0.0:$PORT
celeryd: newrelic-admin run-program python django/manage.py celeryd -E -B --loglevel=INFO
