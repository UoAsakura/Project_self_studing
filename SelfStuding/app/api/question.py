from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..core.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Question)
def create_question(question_data: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.question.create_question(db=db, question_data=question_data)

@router.get("/{question_id}", response_model=schemas.Question)
def get_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.question.get_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@router.get("/", response_model=list[schemas.Question])
def get_questions_for_test(test_id: int, db: Session = Depends(get_db)):
    return crud.question.get_questions_for_test(db, test_id=test_id)
