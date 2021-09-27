from pf_sqlalchemy.db.orm import Base, database


class Contact(Base):
    name = database.Column("name", database.String())
    email = database.Column("email", database.String(100))
    username = database.Column("username", database.String(100))
    password = database.Column("password", database.String(150))

