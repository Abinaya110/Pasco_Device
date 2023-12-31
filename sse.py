from flask import Flask, render_template
from flask_sse import sse

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://localhost:6379'
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/publish')
def publish():
    sse.publish({'message': 'Hello, world!'}, type='greeting')
    return 'Message sent!'

if __name__ == '__main__':
    app.run()