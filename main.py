from flask import Flask, request
from os import environ as envv
from vk_api import VkApi, VkUpload
from vk_api.utils import get_random_id as rand
from vk_api.keyboard import VkKeyboard

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return 'hello world'

@app.route('/add_photos',methods=['POST','GET'])
def add_photos(): pass

@app.route(envv['BOT_ADDRESS'], methods=['POST'])
def bot():
    data = request.get_json(force=True,silent=True)
    if not data or 'type' not in data: return 'not ok'
    if data['secret'] == envv['SECRET_KEY']:
        if data['type'] == 'confirmation': return envv['CONFIRMATION_KEY']
        if data['type'] == 'message_new':
            message = data['object']['message']
            if message['text'] == 'начать': sendMessage(peer_id=message['peer_id'],
                                                        random_id=rand(),message=envv['START_MESSAGE'],
                                                        keyboard=keyboard.get_keyboard())

    return 'ok'

if __name__ in "__main__":
    botSession = VkApi(token=envv['VK_API_KEY'])
    bs = botSession.get_api()
    sendMessage = bs.messages.send
    vupl = VkUpload(bs)

    keyboard = VkKeyboard()
    keyboard.add_button('Хочу картинку')
    keyboard.add_line()
    keyboard.add_button('О мне')

    app.run(host=envv['IP_ADDRESS'],port=envv['PORT'],debug=True)