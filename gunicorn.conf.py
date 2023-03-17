import os

bind = ":8000"
workers = os.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
