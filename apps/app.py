# from pathlib import Path   # 파일 경로나 디렉터리를 쉽게 조작할 수 있도록 돕습니다.
from flask import Flask    #  웹 애플리케이션을 생성하고 요청, 라우팅 등을 처리
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf.csrf import CSRFProtect

from apps.config import config

db = SQLAlchemy()   #  나중에 Flask 앱과 연결되면 데이터베이스 모델을 정의하거나 쿼리를 실행할 수 있음.
csrf = CSRFProtect()

# config 객체 읽어들이기
def create_app(config_key):
    app = Flask(__name__)
    app.config.from_object(config[config_key])
        
    
    csrf.init_app(app)   # CSRF 보호 초기화
    db.init_app(app)     # SQLAlchemy 초기화
    Migrate(app, db)     # 마이그레이션 설정

    
    from apps.todo import views as todo_views
    app.register_blueprint(todo_views.todo, url_prefix="/todo")
    # Blueprint는 Flask의 모듈화 기능으로, 애플리케이션의 기능을 여러 파일로 나누어 관리할 수 있도록 도와줌.

    return app 
    # 구성된 Flask 애플리케이션 객체를 반환.




