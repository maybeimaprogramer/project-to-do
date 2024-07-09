import streamlit as st
import requests
import hashlib


def read_user(username, password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    hashed_password = hash_object.hexdigest()
    
    response = requests.post("http://127.0.0.1:8000/read_user",
                             params={"user_name": username, "user_password": hashed_password})
    
    return response.json()

def display_status(response):
    status = response.get("status")
    message = response.get("message")
    if status == 404:
        st.error("User not found.")
    elif status == 403:
        st.error("Wrong password.")
    elif status == 203:
        st.success("User successfully authenticated.")
        st.write(message)  # Display any additional message from the backend
        
        
username = st.text_input(label="Please input your username:", placeholder="Username")
password = st.text_input(label="Please input your password:", placeholder="Password", type="password")

if st.button("Submit") and username and password:
    response = read_user(username, password)
    display_status(response)


#password found 203
#password not found 403