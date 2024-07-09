from fastapi import FastAPI,Depends
app:FastAPI= FastAPI()
from database import localsession,User,Tasks
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from dotenv import load_dotenv
import os
def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()
# ----------------------------------
# user crud starts here
# ----------------------------------
@app.post("/create_user")
def create_user(user_name:str ,user_password:str , user_firstname:str , user_lastname:str , db: Session = Depends(get_db)):
    try:
        # Create a new user object
        user = User(username=user_name,password=user_password,firstname=user_firstname,lastname=user_lastname)
        print(user)
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"message": "User added successfully", "status": 200}
    except Exception as e:
        db.rollback()  # Rollback the transaction if an error occurs
        return {"message": f"Failed to add user: {str(e)}", "status": 500}






@app.post("/read_user")
def read_user(user_name: str, user_password: str):
    db = localsession()
    user = db.query(User).filter(User.username == user_name).first()

    if user is None:
        return {"message": "User not found", "status": 404}
    elif user.password != user_password:
        return {"message": "Wrong password", "status": 403}
    else:
        return {"message": "Logged in successfully", "status": 203}


# ----------------------------------
# user crud ends here
# ----------------------------------
# ----------------------------------
# tasks crud starts here
# ----------------------------------
@app.post("/create_task")
def gettaskdata(task_name:str,task_desc:str)->None:
    # create a new user
    db=localsession()
    record=Tasks(taskname=task_name,taskdescription=task_desc,userid=1)
    #localsession.add(user)
    #second method
    db.add(record)
    db.commit()
    db.refresh(record)
    print(record)
    return {"message":"tasks addes successfully","status":202}


@app.get("/read_task")
def getask(userid:str,db:Session=Depends(get_db)):
    try:
        tasks=db.query(Tasks).filter(Tasks.userid==userid).all()
        return {"message":tasks,"status":200}
    except Exception as a:
        return {"message":f"Failed to read tasks: {str(a)}","status":500}

@app.delete("/delete_task")
def delete_task(taskid: str, db: Session = Depends(get_db)):
    try:
        db.query(Tasks).filter(Tasks.taskid == taskid).delete()
        db.commit()
        return {"message": "task deleted successfully", "status": 200}
    except Exception as d:
        return {"message": f"Failed to delete task: {str(d)}", "status": 500}


@app.patch("/update_task")
def update_task(taskid: str, task_name: str, task_desc: str, db: Session = Depends(get_db)):
    try:
        db.query(Tasks).filter(Tasks.taskid == taskid).update({"taskname":task_name,"taskdescription":task_desc})
        db.commit()
        return {"message": "task updated successfully", "status": 200}
    except Exception as a:
        return {"message": f"Failed to update task: {str(a)}", "status":500}
                            

# ----------------------------------
# tasks crud ends here
# ----------------------------------












if __name__=="__main__":
    
    import uvicorn
    uvicorn.run("server:app",reload=True)
