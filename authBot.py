from flask import Flask, request
import hashlib

app = Flask(__name__)
BOT_TOKEN = "7901063068:AAFL955WOGlXooiiMXDWmv_N0LSgi5B-JrM"

def check_telegram_auth(data):
    check_hash = data.pop("hash")
    data_check_string = "\n".join(
        [f"{k}={v}" for k, v in sorted(data.items())]
    )
    secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()
    calculated_hash = hashlib.sha256(data_check_string.encode()).hexdigest()
    return check_hash == calculated_hash

@app.route("/auth", methods=["GET", "POST"])
def auth():
    data = request.args.to_dict() if request.method == "GET" else request.form.to_dict()
    if check_telegram_auth(data):
        return f"Добро пожаловать, {data['first_name']}!"
    else:
        return "Ошибка авторизации!", 403

if __name__ == "__main__":
    app.run()
