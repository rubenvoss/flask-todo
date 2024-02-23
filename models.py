from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class Task(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    done: so.Mapped[bool] = so.mapped_column(sa.Boolean(), nullable=False, default=False)

    def __repr__(self):
        return '<Task {}>'.format(self.name)
