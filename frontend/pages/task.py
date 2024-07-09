import streamlit as st 
import hashlib 
import requests




def createtask ():
    requests.post("http://127.0.0.1:8000/create_task",params={"task_name":taskname,"task_desc":taskdesc})
taskname:str=st.text_input(label="please input yout taskname: ",placeholder="taskname")
taskdesc:str=st.text_input(label="please input yout taskdesc: ",placeholder="taskdesc")
if  taskname and taskdesc :
    st.button("submit",on_click=createtask())
else:
    st.button("submit",on_click="",disabled=True)



