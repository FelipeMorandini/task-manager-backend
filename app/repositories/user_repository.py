from .base_repository import BaseRepository
from ..models.User import User
from ..utils.hashing import hash_password, verify_password

from ..database.connection import Session

class UserRepository(BaseRepository):

    def signup(self, db: Session, user: dict):
        user['password'] = hash_password(user['password']) 
        return super().create(db, user)

    def login(self, db: Session, username: str, password: str):
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        return user

    def reset_password(self, db: Session, user_id: int, new_password: str):
        user = super().get(db, user_id)
        if not user:
            return False
        user.password = hash_password(new_password)
        db.commit()
        return True