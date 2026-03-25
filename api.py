import os
from flask import Flask
from sqlalchemy import text
from app.models.database import db
from routes.webhook import webhook_bp

from app.models import messageHistory, reservation, user, preReservationStep
from app.mock.model_mock import RoomType, RoomOccupancy, Room ##PARA MOCK
from app.mock.data_mock import load_mock_data

REQUIRED_ENV_VARS = [
    'DATABASE_CONNECTION_URI',
    'GROQ_API_KEY',
    'HUGGINGFACE_API_KEY',
    'LLAMA_V'
]

def validate_env():
    missing = [var for var in REQUIRED_ENV_VARS if not os.environ.get(var)]
    if missing:
        raise EnvironmentError(f"ERRO: Variáveis de ambiente faltando: {', '.join(missing)}")

validate_env()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_CONNECTION_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    engine = db.get_engine()
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS hotel"))
        conn.commit()

    db.create_all()
    
    # Carrega dados mockados apenas se configurado (evita resetar dados em produção)
    if os.environ.get('LOAD_MOCK_DATA', 'false').lower() == 'true':
         load_mock_data()

app.register_blueprint(webhook_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
