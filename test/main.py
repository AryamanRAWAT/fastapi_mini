from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from database import Base, SessionLocal, engine
from models import Users
from sqlalchemy.orm import Session
from schemas import UserSchema

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users", response_model=List[UserSchema])
def get(db:Session=Depends(get_db)):
    users = db.query(Users).all()
    return users

@app.post("/create",response_model=UserSchema)
def post(request:UserSchema,db:Session=Depends(get_db)):
        user = Users(
                        id = request.id, 
                        first_name = request.first_name,
                        last_name = request.last_name,
                        age = request.age,
                        city = request.city,
                        state = request.state,
                        zip = request.zip,
                        email = request.email,
                        web = request.web
                        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return 'User Created!'

@app.put("/update/{pk}",response_model=UserSchema)
def put(pk:int,request:UserSchema,db:Session=Depends(get_db)):
    try:
        u = db.query(Users).filter(Users.id==pk).first()
        u.first_name = request.first_name,
        u.last_name = request.last_name,
        u.age = request.age,
        db.add(u)
        db.commit()
        db.refresh(u)
        return "User Updated"
    except:
         return HTTPException(status_code=404,detail="user not found")
    

@app.delete("/users/{user_id}", response_class=JSONResponse)
def delete_user(user_id: int, db: Session=Depends(get_db)):
    try:
        u=db.query(Users).filter(Users.id ==user_id).first()
        db.delete(u)
        db.commit()
        return {f"user of id {user_id} has been deleted": True}
    except:
        return HTTPException (status_code=404, detail="user not found")