import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis',port=6379)

def get_hit_count():
	retries = 5
	while True:
		try:
			return cache.incr('hit')
		except redis.exception.ConnectionError as exc:
			if retries == 0:
				return exc
			retries -= 1
			time.sleep(0.5)

@app.route('/')
def hello():
	count = get_hit_count()
	return f"Hello world! Page has been visited by {count} times."



