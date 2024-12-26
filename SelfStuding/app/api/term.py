from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..core.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Term)
def create_term(term_data: schemas.TermCreate, db: Session = Depends(get_db)):
    return crud.term.create_term(db=db, term_data=term_data)

@router.get("/{term_id}", response_model=schemas.Term)
def get_term(term_id: int, db: Session = Depends(get_db)):
    db_term = crud.term.get_term(db, term_id=term_id)
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return db_term

@router.get("/", response_model=list[schemas.Term])
def get_terms_for_subtopic(subtopic_id: int, db: Session = Depends(get_db)):
    return crud.term.get_terms_for_subtopic(db, subtopic_id=subtopic_id)
