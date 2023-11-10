import os
import databases
import sqlalchemy
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")

database=databases.Database(DATABASE_URL)

metadata=sqlalchemy.MetaData()

notes=sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer,
                      primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

engine=sqlalchemy.create_engine(
    DATABASE_URL
)
# metadata.create_all(engine)

class NoteIn(BaseModel):
    text: str
    completed: bool

class Note(BaseModel):
    id: int
    text: str
    completed: bool

app=FastAPI()

origins=[
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/notes/", response_model=List[Note])
async def read_notes():
    query=notes.select()
    return await database.fetch_all(query)

@app.get("/notes/{note_id}", response_model=Note)
async def read_note(note_id: int):
    existing_note=await database.fetch_one(notes.select().where(notes.c.id==note_id))
    if existing_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
        
    return existing_note
    

@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    print(note)
    query=notes.insert().values(text=note.text,
                                completed=note.completed)
    last_record_id=await database.execute(query)
    return {**note.dict(), "id":last_record_id}

@app.delete("/notes/{note_id}", response_model=dict)
async def delete_note(note_id: int):
    existing_note=await database.fetch_one(notes.select().where(notes.c.id==note_id))
    if existing_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    delete_query=notes.delete().where(notes.c.id==note_id)
    await database.execute(delete_query)
    return {"message":"Note deleted successfully."}

@app.put("/notes/{note_id}", response_model=Note)
async def update_note(note_id: int, updated_note: NoteIn):
    existing_note=await database.fetch_one(notes.select().where(notes.c.id==note_id))
    if existing_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    update_query=notes.update().where(notes.c.id==note_id).values(
        text=updated_note.text,
        completed=updated_note.completed
    )
    await database.execute(update_query)
    
    updated_note_data={**existing_note, "text":updated_note.text, "completed": updated_note.completed}
    return updated_note_data

@app.get("/")
def read_root():
    return {"Hello":"World"}