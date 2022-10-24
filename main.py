from flask import Flask, request, render_template
from os import environ as envv, listdir
from vk_api import VkApi, VkUpload
from vk_api.utils import get_random_id as rand
from vk_api.keyboard import VkKeyboard

app = Flask(__name__,template_folder='templates')

@app.route('/',methods=['POST','GET'])
def index():
    return 'hello world'

@app.route('/add_photos',methods=['POST','GET'])
def add_photos():
    if request.method == 'POST':
        pass

    return render_template('add_photos.html', photos=listdir('photos'))

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

            elif message['text'] == f'{envv["TO_BOT"]} О мне': sendMessage(peer_id=message['peer_id'],
                                                          random_id=rand(),message=envv['ABOUT_MESSAGE'],
                                                          attachment=envv['ABOUT_ATTACHMENT'])

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