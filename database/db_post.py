from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
import datetime
from database.models import DbPost
from fastapi import HTTPException, status


def create(db:Session, request: PostBase):
    new_post = DbPost(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db: Session):
    return db.query(DbPost).all()

def delete_post(id: int, db: Session):
     db_post = db.query(DbPost).filter(DbPost.id == id).first()
     if not db_post:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The ID {id} was not found")
     if db_post is not None:
        db.delete(db_post)
        db.commit()
     return db_post


