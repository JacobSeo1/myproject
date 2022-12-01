from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # config.py 파일에 작성한 항목을 읽어냄
    app.config.from_object(config)
    # ORM
    # SQLALCHEMY에 app 등록
    db.init_app(app)
    # Migrate에 app(Flask)과 db(SQLAlchemy) 등록
    migrate.init_app(app, db)

    # 블루프린트 등록
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app