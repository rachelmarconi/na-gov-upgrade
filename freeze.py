from flask_frozen import Freezer
from app import app, get_activity_csv
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()