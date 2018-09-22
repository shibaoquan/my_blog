from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Role(db.Model):
    __tablename__ = "roles"  # 表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role")

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, index=True)  # 创建索引
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return '<User %r>' % self.username

    password_hash = db.Column(db.String(128))


    @property
    def password(self):
        raise AttributeError('password is not a readbale attribute')

    @password.setter   # 设置密码
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):  # 校验密码
        return  check_password_hash(self.password_hash, password)








