from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..core.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Topic)
def create_topic(topic_data: schemas.TopicCreate, db: Session = Depends(get_db)):
    return crud.topic.create_topic(db=db, topic_data=topic_data)

@router.get("/{topic_id}", response_model=schemas.Topic)
def get_topic(topic_id: int, db: Session = Depends(get_db)):
    db_topic = crud.topic.get_topic(db, topic_id=topic_id)
    if db_topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return db_topic

@router.get("/", response_model=list[schemas.Topic])
def get_all_topics(db: Session = Depends(get_db)):
    return crud.topic.get_all_topics(db)
