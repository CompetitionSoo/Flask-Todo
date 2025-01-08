from datetime import datetime
from apps.app import db
from werkzeug.security import check_password_hash

class Todo(db.Model) :
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)               # 할일 항목의 고유 ID
    content = db.Column(db.String)                             # 내용 
    is_done = db.Column(db.Boolean, default=False)             # 완료여부
    created_at = db.Column(db.DateTime, default=datetime.now)  # 생성시간(기본값: 현재시간)





