from flask import Flask
from flask import request
import redis
import json

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/api/set_static', methods=['POST'])
def set_static():
    content = request.get_json()
    print(content)
    r.set('laser/animation_strategy', 'static')
    r.set('laser/static_animation', content['static_animation'])
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
