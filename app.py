from flask import Flask, render_template, request, jsonify, make_response, json
from pusher import pusher

app = Flask(__name__)

pusher = pusher_client = pusher.Pusher(
    app_id='1020106',
    key='7ee7287be8e1a6e27c4d',
    secret='077245e046c24855b049',
    cluster='ap1',
    ssl=True
)

name = ''

@app.route('/')
def index():
  return render_template('index.html')
@app.route('/test')
def test():
  global name
  name = request.args.get('username')
  return render_template('test.html')
#@app.route('/play')
#def play():
  #global name
  #name = request.args.get('username')
  #return render_template('play.html')
@app.route('/testjson', methods=['POST'])
def testjson():
    global data
    data = request.get_json()
    text = data['text']
    hint = data['hint']
    wordkey = data['key']
    return jsonify({'text' : text[1], 'hint' : hint[1], 'wordkey' : wordkey[1]})
@app.route("/pusher/auth", methods=['POST'])
def pusher_authentication():
  auth = pusher.authenticate(
    channel=request.form['channel_name'],
    socket_id=request.form['socket_id'],
    custom_data={
      u'user_id': name,
      u'user_info': {
        u'role': u'player'
      }
    }
  )
  return json.dumps(auth)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

name = ''