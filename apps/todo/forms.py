from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

# StringField : 문자열입력필드를 생성
# SubmitField : 제출버튼을 생성
# DataRequired 입력이 없으면 에러 메시지를 반환.
# Length : 입력값의 길이를 제한 <최소, 최대를 지정할수있음>

# validators  메시지: 입력이 없을 경우, "이 필드는 필수 항목입니다.
# name = StirngField(
#        name,
#  validators=[DataRequired(message="이 필드는 필수 항목입니다.")])

class TodoForm(FlaskForm):
    content = StringField(
        "할일",
        validators=[
            DataRequired(message="필수항목을 적어주시기 바랍니다."),
            Length(max=20, message="최대길이는 20자 이내로 작성하여주시기바랍니다.")
        ]
    )
    submit = SubmitField("추가")