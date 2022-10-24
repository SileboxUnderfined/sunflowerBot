from flask import Flask, request
from os import environ as envv
from vk_api import VkApi, VkUpload

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return 'hello world'

@app.route('/add_photos',methods=['POST','GET'])
def add_photos(): pass

@app.route(envv['BOT_ADDRESS'], methods=['POST'])
def bot():
    data = request.get_json(force=True,silent=True)

    return 'ok'

if __name__ in "__main__":
    botSession = VkApi(token=envv['VK_API_KEY'])
    bs = botSession.get_api()
    vupl = VkUpload(bs)

    app.run(host=envv['IP_ADDRESS'],port=envv['PORT'],debug=True)