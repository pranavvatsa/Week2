from datetime import datetime
import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://root:root@cluster0.bl2mpwc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
print(client)
db = client['test']  # Replace 'your_database_name' with your MongoDB database name
users_collection = db['users']

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }

def login_user(username, password):
    user = users_collection.find_one({'username': username, 'password': password})
    if user:
        return True, 'Login successful'
    else:
        return False, 'Invalid username or password'
def main():
    st.title('E-commerce Web Application')
    st.subheader('User Authentication')
    login_username = st.text_input('Username (Login)')
    login_password = st.text_input('Password (Login)', type='password')
    if st.button('Login'):
        success, message = login_user(login_username, login_password)
        st.write(message) 
        
if __name__ == '__main__':
    main()