#colab에서 

!pip install Flask pyngrok


------------------------------------------------------------------------

import threading
from flask import Flask
from pyngrok import ngrok  # pyngrok 모듈 가져오기 추가

# 1. ngrok 인증 토큰 설정 (필수!)
# 토큰 확인 주소: https://ngrok.com
NGROK_TOKEN = "여기에_토큰을"
ngrok.set_auth_token(NGROK_TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>구글 코랩에서 열심히 공부해요!</h1>"

def run_app():
    # 코랩 환경 충돌 방지를 위해 debug=False, use_reloader=False 설정
    app.run(port=5000, debug=False, use_reloader=False)

# 2. Flask를 백그라운드 스레드에서 실행
threading.Thread(target=run_app).start()

# 3. ngrok 터널을 열어 외부 접속 주소 생성
# 포트 번호는 문자열 또는 숫자로 지정 가능하며, 프로토콜 명시가 안전합니다.
tunnel = ngrok.connect(5000, "http")
print("이 주소로 접속하세요:", tunnel.public_url)

