from app import create_app, db
from app.models import User

app = create_app()

def init_database():
    with app.app_context():
        db.create_all()
        print("Database tables created succesfully.")


if __name__ == "__main__":
    init_database()