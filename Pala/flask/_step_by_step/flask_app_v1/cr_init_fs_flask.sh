#!/bin/bash

file_name="/home/st/REPOBARE/_repo/NPython/Pala/flask/_step_by_step/flask_app/cr_init_fs_flask.sh"

plt_vae "cd $(dirname ${file_name})"

touch __init__.py
touch app.py

mkdir -p templates

touch templates/about.html
touch templates/events.html
touch templates/index.html

mkdir -p templates/bootstrap
touch templates/bootstrap/base.html

mkdir -p static
