#!/bin/bash

# GET THE UPLOAD URL
UPLOAD_URL=`curl -s http://localhost:9001/gimme-upload-url/` 

echo "UPLOADING TO: $UPLOAD_URL \n"

# POST THE MAGIC FILE FULL OF UNICORNS AND HAPPINESS TO THE UPLOAD URL
curl --form "fairydust=@MAGIC_FILE" $UPLOAD_URL
