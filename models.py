from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin

db = SQLAlchemy()

roles_users_table = db.Table(
    "roles_users",
    db.Column("users_id", db.Integer(), db.ForeignKey("users.id")),
    db.Column("roles_id", db.Integer(), db.ForeignKey("roles.id")),
)


class Roles(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(80))
    active = db.Column(db.Boolean())

    roles = db.relationship("Roles", secondary=roles_users_table, backref="user", lazy=True)