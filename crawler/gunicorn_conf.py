import logging
import os

bind = "0.0.0.0:8000"
max_requests = 1000
workers = 5
max_requests_jitter = 100
worker_class = "gevent"
capture_output = True
access_logfile = '-'