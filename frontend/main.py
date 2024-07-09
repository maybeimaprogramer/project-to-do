import streamlit as st
import requests

st.write("# :blue[momin faisal]")
st.write("### :red[task left : 14]")
st.write("<hr>",unsafe_allow_html=True)
"""
1.get users tasks
2.add new task
3. update task
4.delete task

"""


def readtask(userid=1):
    response = requests.get("http://127.0.0.1:8000/read_task", params={"userid": userid})
    return response.json()['message']


def dele(taskid):
    response = requests.delete("http://127.0.0.1:8000/delete_task", params={"taskid": taskid})

def upd(taskid,taskname,taskdesc):
    response=requests.patch("http://127.0.0.1:8000/update_task",params={"taskid":taskid,"task_name":taskname,"task_desc":taskdesc})
   

# Fetch the tasks   
tasks = readtask()

# Display each task with its name, description, and buttons
for task in tasks:
    st.write(f"**Task Name:** {task['taskname']}")
    st.write(f"**Task Description:** {task['taskdescription']}")
    
    update_button = st.button("Update", key=f"update_{task['taskid']}")
    delete_button = st.button("Delete", key=f"delete_{task['taskid']}")

    if update_button:
        taskname:str=st.text_input(label="please input yout taskname: ",placeholder="taskname")
        taskdesc:str=st.text_input(label="please input yout taskdesc: ",placeholder="taskdesc")
        upd(task['taskid'],taskname,taskdesc)
        
            

        st.write(f"Update button clicked for task {task['taskid']}")
        
    if delete_button:
     dele(task["taskid"])
     st.write(f"Delete button clicked for task {task['taskid']}")









