from pathlib import Path
# 공통설정 정의
class BaseConfig :
    SECRET_KEY="1234"          # Flask 보안 키, 세션과 쿠키를 암호화하는 데 사용됩니다.
    WTF_CSRF_SECRET_KEY="1234" # CSRF 보안키

# 로컬 환경에서 사용되는 설정
class LocalConfig(BaseConfig) :
    SQLALCHEMY_DATABASE_URI="sqlite:///"+ str(Path(Path(__file__).parent.parent, 'local.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True       # SQL 쿼리를 출력 (디버깅용).

# 테스트 환경에서 사용되는 설정
class TestingConfig(BaseConfig) :
    SQLALCHEMY_DATABASE_URI="sqlite:///"+ str(Path(Path(__file__).parent.parent, 'local.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    WTF_CSRF_ENABLED=False

config = {
    "testing" : TestingConfig,
    "local" : LocalConfig
}