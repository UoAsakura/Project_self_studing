from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..core.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.SubTopic)
def create_subtopic(subtopic_data: schemas.SubTopicCreate, db: Session = Depends(get_db)):
    return crud.subtopic.create_subtopic(db=db, subtopic_data=subtopic_data)

@router.get("/{subtopic_id}", response_model=schemas.SubTopic)
def get_subtopic(subtopic_id: int, db: Session = Depends(get_db)):
    db_subtopic = crud.subtopic.get_subtopic(db, subtopic_id=subtopic_id)
    if db_subtopic is None:
        raise HTTPException(status_code=404, detail="Subtopic not found")
    return db_subtopic

@router.get("/", response_model=list[schemas.SubTopic])
def get_subtopics_for_topic(topic_id: int, db: Session = Depends(get_db)):
    return crud.subtopic.get_subtopics_for_topic(db, topic_id=topic_id)
