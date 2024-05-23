#!/bin/sh

echo "UPLOAD EXECUTION TIME: $(date)" >> runtime.out >> runtime.err
python3 -u main.py >> runtime.out 2>> runtime.err &
