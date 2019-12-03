from application import db
from application.models.role import account_role

from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    users_reservations = db.relationship("Reservation", backref = "account")
    users_roles = db.relationship("Role", secondary = account_role, back_populates = "roles_users")

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        stmt = text("""SELECT r.name FROM role r
                     JOIN account_role ar ON r.id = ar.role_id
                     WHERE ar.account_id = :self_id"""
                    ).params(self_id = self.id)
        roles = db.engine.execute(stmt)

        response = []
        for row in roles:
            response.append(row[0])
        
        return response

    def add_role(self, role):
        stmt = text("""SELECT r.id FROM role r
                     WHERE r.name = :role"""
                    ).params(role = role)
        role_id = db.engine.execute(stmt).fetchone()

        print(role_id)

        self.users_roles.append(role_id[0])