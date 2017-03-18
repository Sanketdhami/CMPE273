from flask import Flask
import requests,json,base64
from flask import request
from flask import jsonify
import sys
uri=sys.argv[1]
uri_list = uri.split('/')
user=uri_list[3]
repository = uri_list[4]
app = Flask(__name__)

@app.route("/v1/dev-config.yml")
def hello():
        url="https://api.github.com/repos/"+user+"/"+repository+"/contents/dev-config.yml"
        get_response = requests.get(url)
        s = get_response.json()
        data=base64.decodestring(s['content'])
        return data

@app.route("/v1/test-config.yml")
def hello1():
        url="https://api.github.com/repos/"+user+"/"+repository+"/contents/test-config.yml"
        get_response = requests.get(url)
        s = get_response.json()
        data=base64.decodestring(s['content'])
        return data

@app.route("/v1/dev-config.json")
def hello2():
        url="https://api.github.com/repos/"+user+"/"+repository+"/contents/dev-config.json"
        get_response = requests.get(url)
        s = get_response.json()
        data=base64.decodestring(s['content'])
        json_data = json.dumps(data)
        return json.loads(json_data)

@app.route("/v1/test-config.json")
def hello3():
        url="https://api.github.com/repos/"+user+"/"+repository+"/contents/test-config.json"
        get_response = requests.get(url)
        s = get_response.json()
        data=base64.decodestring(s['content'])
        json_data = json.dumps(data)
        return json.loads(json_data)

if __name__ == "__main__":
        app.run(debug=True,host='0.0.0.0')
