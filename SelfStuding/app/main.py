from fastapi import FastAPI
from .api import user, topic, subtopic, term, test, question

app = FastAPI()

# Регистрация маршрутов
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(topic.router, prefix="/topics", tags=["topics"])
app.include_router(subtopic.router, prefix="/subtopics", tags=["subtopics"])
app.include_router(term.router, prefix="/terms", tags=["terms"])
app.include_router(test.router, prefix="/tests", tags=["tests"])
app.include_router(question.router, prefix="/questions", tags=["questions"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Test Creator API"}