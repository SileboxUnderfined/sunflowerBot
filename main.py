from flask import Flask, request
from os import environ as envv
from vk_api import VkApi, VkUpload

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return 'hello world'

@app.route('/add_photos',methods=['POST','GET'])
def add_photos(): pass

@app.route(envv['BOT_ADDRESS'], methods=['POST','GET'])
def bot():
    data = request.get_json(force=True,silent=True)
    if not data or 'type' not in data: return 'not ok'
    if data['secret'] == envv['SECRET_KEY']:
        if data['type'] == 'confirmation' and data['group_id'] == envv['GROUP_ID']: return envv['CONFIRMATION_KEY']
    return 'ok'

if __name__ in "__main__":
    botSession = VkApi(token=envv['VK_API_KEY'])
    bs = botSession.get_api()
    vupl = VkUpload(bs)

    app.run(host=envv['IP_ADDRESS'],port=envv['PORT'],debug=True)