import os
# DB파일은 프로젝트 홈 디렉터리 바로 밑에 저장 됨.
BASE_DIR = os.path.dirname(__file__)
# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLALCHEMY의 이벤트 처리옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False