bind = "unix:/run/gunicorn-aane.sock"
workers = 3
worker_class = "sync"
timeout = 120
keepalive = 2
max_requests = 1000
max_requests_jitter = 100