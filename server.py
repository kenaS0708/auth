from flask import Flask, request, jsonify
from hashlib import sha256
from hmac import new as hmac_new
import os

app = Flask(__name__)

# Секретный токен вашего бота (получите его у BotFather)
BOT_TOKEN = "7901063068:AAFL955WOGlXooiiMXDWmv_N0LSgi5B-JrM"
SECRET_KEY = sha256(BOT_TOKEN.encode()).digest()


def verify_telegram_auth(data):
    """Проверка подлинности данных от Telegram"""
    auth_data = {k: v for k, v in data.items() if k != 'hash'}
    check_string = '\n'.join([f"{k}={v}" for k, v in sorted(auth_data.items())])
    secret_hash = hmac_new(SECRET_KEY, check_string.encode(), sha256).hexdigest()
    return secret_hash == data.get('hash')


@app.route('/auth', methods=['GET'])
def auth():
    # Получаем параметры из URL
    data = request.args.to_dict()

    # Проверяем данные на подлинность
    if not verify_telegram_auth(data):
        return jsonify({'error': 'Invalid authentication data'}), 403

    # Вытаскиваем информацию о пользователе
    telegram_id = data.get('id')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    username = data.get('username', '')

    # Здесь вы можете обработать авторизацию пользователя, например, сохранить его в базе данных
    return jsonify({
        'message': 'Authentication successful',
        'user': {
            'telegram_id': telegram_id,
            'first_name': first_name,
            'last_name': last_name,
            'username': username
        }
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Port для Render
    app.run(host="0.0.0.0", port=port)
