from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='redis',decode_responses=True)

@app.route('/')
def home():
	visit_count = redis_client.incr('visit')
	return f"hello from docker, you visit {visit_count} times "
	
@app.route('/reset')
def reset():
	redis_client.delete('visit')
	return "Visit Count reset!"
	
@app.route('/about')
def about():
	return "this pages is still developing"


@app.route('/services')

def services():
	return "this pages is all about services!"

@app.route('/faq')
def faq():
	return "this page is all about Frequently ask Question"

@app.route('/Team')
def Team():
	return "This page is about our Team Member"


if __name__ == '__main__':

	app.run(host="0.0.0.0",port=5000)
