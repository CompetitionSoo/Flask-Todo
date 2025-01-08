from apps.app import db
from apps.todo.models import Todo     # 데이터베이스에서 사용할 모델을 가져옵니다
from apps.todo.forms import TodoForm  # 사용자로부터 할 일 내용을 입력받을 폼
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

# Blueprint 생성한다
todo = Blueprint(
    "todo",
    __name__,
    template_folder="templates",
    static_folder="static",
    # Blueprint에서 사용할 템플릿과 정적 파일의 폴더 위치를 지정합니다.
)

# Index 페이지 (할 일 목록 표시 및 추가)
@todo.route("/", methods=["GET", "POST"])
@login_required
def index() :
    form = TodoForm()
    if request.method == "POST" :
        if form.validate_on_submit() : 
            todo = Todo(                   # Todo 모델 인스턴스 생성
                content=form.content.data  # 폼에서 입력받은 할 일 내용
            )
            db.session.add(todo)           # 할 일 항목을 세션에 추가  
            db.session.commit()            # 변경사항을 데이터베이스에 커밋

            return redirect(url_for("todo.index"))  
            # 새로 고침하여 할 일 목록으로 리디렉션

    todos = Todo.query.all()               # 모든 할 일 항목을 가져옵니다.
    return render_template("todo/index.html", todos=todos, form=form)



## 할 일 삭제
@todo.route("/delete/<todo_id>", methods=["GET", "POST"])
@login_required
def delete(todo_id) :
    form = TodoForm() # 삭제페이지에 사용할 폼 생성

    todo = Todo.query.filter_by(id=todo_id).first()
    if request.method == "POST" :
        db.session.delete(todo)
        db.session.commit()

        return redirect(url_for("todo.index"))
    return render_template("todo/delete.html", todo=todo, form=form)