from app import create_app
from config import config_by_name
import os
from dotenv import load_dotenv

# Carica le variabili d'ambiente dal file .env
load_dotenv()

config_name = os.getenv('FLASK_ENV', 'development')
app = create_app(config_class=config_by_name[config_name])

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
