#!/bin/bash

/home/rick/.local/bin/gunicorn -c gunicorn.ini 'dj_project.wsgi:application'

