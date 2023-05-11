#!/bin/bash

tar --exclude='./.git' --exclude='./.venv' --exclude='./.gitignore' -zcvf test-blog.tar .

