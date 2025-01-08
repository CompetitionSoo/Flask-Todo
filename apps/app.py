# from pathlib import Path   # 파일 경로나 디렉터리를 쉽게 조작할 수 있도록 돕습니다.
from flask import Flask      #  웹 애플리케이션을 생성하고 요청, 라우팅 등을 처리
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager   

from apps.config import config

db = SQLAlchemy()   #  나중에 Flask 앱과 연결되면 데이터베이스 모델을 정의하거나 쿼리를 실행할 수 있음.
csrf = CSRFProtect()
login_manager = LoginManager() # Flask-Login 객체, 로그인 관련 작업을 처리


# 로그인 뷰 설정: 로그인하지 않은 사용자가 접근할 때 리다이렉트할 URL 지정
login_manager.login_view = "auth.signup"
# 로그인 메시지를 빈 문자열로 설정 (기본 메시지를 사용하지 않음)
login_manager.login_message = ""


# config 객체 읽어들이기
def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(config[config_key])
        
    
    csrf.init_app(app)   # CSRF 보호 초기화
    db.init_app(app)     # SQLAlchemy 초기화
    Migrate(app, db)     # 마이그레이션 설정
    login_manager.init_app(app)
    
    from apps.todo import views as todo_views
    app.register_blueprint(todo_views.todo, url_prefix="/todo")
    # Blueprint는 Flask의 모듈화 기능으로, 애플리케이션의 기능을 여러 파일로 나누어 관리할 수 있도록 도와줌.

    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app 
    # 구성된 Flask 애플리케이션 객체를 반환.




