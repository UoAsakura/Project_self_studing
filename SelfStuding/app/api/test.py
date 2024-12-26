from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..core.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Test)
def create_test(test_data: schemas.TestCreate, db: Session = Depends(get_db)):
    return crud.test.create_test(db=db, test_data=test_data)

@router.get("/{test_id}", response_model=schemas.Test)
def get_test(test_id: int, db: Session = Depends(get_db)):
    db_test = crud.test.get_test(db, test_id=test_id)
    if db_test is None:
        raise HTTPException(status_code=404, detail="Test not found")
    return db_test

@router.get("/", response_model=list[schemas.Test])
def get_tests_for_subtopic(subtopic_id: int, db: Session = Depends(get_db)):
    return crud.test.get_tests_for_subtopic(db, subtopic_id=subtopic_id)
