import getpass
import sys
from models.users import User
from app import app, db, bcrypt

def bootstrap_admin():
    with app.app_context():
        existing_admin = User.query.filter_by(role="admin").first()
        if existing_admin:
            print(f"Admin account '{existing_admin.username}' already exists.")
            sys.exit(1)

        username = input("USERNAME:").strip()

        if User.query.filter_by(username=username).first():
            print(f"Username {username} is already taken.")
            sys.exit(1)

        password = getpass.getpass("PASSWORD:")
        confirmed_password = getpass.getpass("PASSWORD (CONFIRM):")

        if not password or password != confirmed_password:
            print("Password was empty or did not match confirmation.")
            sys.exit(1)

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        admin = User(username=username, password=hashed_password, role="admin")

        db.session.add(admin)
        db.session.commit()
        print(f"SUCCESSFULLY CREATED ADMIN: {username}.")

if __name__ == "__main__":
    bootstrap_admin()