#!/bin/bash

$VIRTUAL_ENV/lib/python2.7/site-packages/google_appengine/dev_appserver.py \
    --allow_skipped_files \
    --admin_port 9100 \
    --port 9000 \
    app.yaml pixieland.yaml
