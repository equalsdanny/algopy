#!/usr/bin/env python3

import time
from datetime import datetime
from requests import Session
import sys

def log(text, exception=None):
    print(text, file=sys.stderr, flush=True)
    if exception is not None:
        print(exception, file=sys.stderr)

s = Session()
log('Fetcher up @ {}'.format(datetime.now().isoformat()))

while True:
    try:
        counter = s.get('https://leetcode.com/submissions/count/').json()['submission_count']
        print('{}_{}'.format(datetime.now().timestamp(), counter), flush=True)
    except Exception as e:
        log('Something went wrong at {}'.format(datetime.now()),e)
    time.sleep(5)
