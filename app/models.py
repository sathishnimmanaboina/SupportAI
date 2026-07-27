from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from app.extensions import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    tickets = db.relationship(
        "Ticket",
        backref="author",
        lazy=True
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"



class Ticket(db.Model):

    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    description = db.Column(db.Text, nullable=False)

    status = db.Column(
        db.String(30),
        default="Open"
    )

    priority = db.Column(
        db.String(30),
        default="Medium"
    )

    category = db.Column(
        db.String(100),
        default="General"
    )

    # ---------- AI Fields ----------
    ai_summary = db.Column(db.Text)

    ai_reply = db.Column(db.Text)

    # -------------------------------

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    def __repr__(self):
        return f"<Ticket {self.title}>"



class KnowledgeBase(db.Model):

    __tablename__ = "knowledge_base"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    uploaded_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<KnowledgeBase {self.title}>"