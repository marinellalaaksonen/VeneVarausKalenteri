from application import db

account_role = db.Table("account_role",
    db.Column("account_id", db.Integer, db.ForeignKey("account.id")), 
    db.Column("role_id", db.Integer, db.ForeignKey("role.id"))
)

class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(144), nullable=False, unique=True)

    roles_users = db.relation("User", secondary = account_role, back_populates = "users_roles")

    def __init__(self, role):
        self.role = role