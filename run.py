from app import app
from app.config import BaseConfig as APP_CONFIG
# from flask_ngrok import run_with_ngrok

# run_with_ngrok(app)

if __name__ == '__main__':
    app.run(APP_CONFIG.APP_HOST, APP_CONFIG.APP_PORT)