from flask import Flask
import redis

app = Flask(__name__)
# Connect to the database
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # Increase the visit counter by 1
    count = cache.incr('visits')
    return f"Hello DevOps World! This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
