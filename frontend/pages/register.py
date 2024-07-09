import streamlit as st
import hashlib 
import requests

# Function to hash the password
def hash_password(password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode())
    return hash_object.hexdigest()

# Function to create a new user via API
def create_user(username, password, firstname, lastname):
    hashed_password = hash_password(password)
    response = requests.post("http://127.0.0.1:8000/create_user", 
                             params={"user_name": username, 
                                   "user_password": hashed_password, 
                                   "user_firstname": firstname, 
                                   "user_lastname": lastname})
    return response.json()

# Streamlit UI elements
username = st.text_input(label="Please input your username:", placeholder="Username")
password = st.text_input(label="Please input your password:", placeholder="Password", type="password")
firstname = st.text_input(label="Please input your firstname:", placeholder="Firstname")
lastname = st.text_input(label="Please input your lastname:", placeholder="Lastname")

# Submit button handling
if st.button("Submit"):
    if username and password and firstname and lastname:
        response = create_user(username, password, firstname, lastname)
        if "message" in response and response["status"] == 200:
            st.success(response["message"])
        else:
            st.error("Failed to create user. Please try again.")
    else:
        st.warning("Please fill in all fields.")

