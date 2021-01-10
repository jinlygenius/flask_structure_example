from databases import mysqldb as db
from sqlalchemy.sql import func


class User(db.Model):

    __tablename__ = 'user'

    # uuid
    id = db.Column(
        db.String(32),
        primary_key=True
    )
    username = db.Column(
        db.String(64),
        index=True,
        unique=True,
        nullable=False
    )
    phone = db.Column(
        db.String(11),
        index=False,
        unique=True,
        nullable=True
    )
    name = db.Column(
        db.String(60),
        index=False,
        unique=False,
        nullable=True
    )
    gender = db.Column(
        db.String(1),
        index=False,
        unique=False,
        nullable=True
    )
    email = db.Column(
        db.String(254),
        index=False,
        unique=True,
        nullable=True
    )
    password = db.Column(
        db.String(128),
        index=False,
        unique=False,
        nullable=True
    )
    created_time = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True,
        default=func.now()
    )
    updated_time = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True,
        default=func.now(),
        onupdate=func.now()
    )

    __mapper_args__ = {
        "order_by": created_time.desc()
    }

    def __repr__(self):
        return f'<User {self.username}>'
