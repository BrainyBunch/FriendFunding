
import pyrebase 

firebaseConfig = {    
    "apiKey": "AIzaSyCd8K3DWSUID6pRZEP3n-cFwvnIBr6maz4",
    "authDomain": "friendfunding-b16a2.firebaseapp.com",
    "databaseURL": "https://friendfunding-b16a2-default-rtdb.firebaseio.com",
    "projectId": "friendfunding-b16a2",
    "storageBucket": "friendfunding-b16a2.appspot.com",
    "messagingSenderId": "409268289779",
    "appId": "1:409268289779:web:bf695d06dcb1dd16f17786",
    "measurementId": "G-KFH3H81R3G"
    }

# telling the computer that we want to initialize this app with this info  
firebase = pyrebase.initialize_app(firebaseConfig)

# db = firebase.database()
# auth = firebase.auth()
storage = firebase.storage() 

#  ====================== Authentication 
# ============== LOGIN
email = input("Enter your email!")
password = input("Enter your password!")
try:
    auth.sign_in_with_email_and_password(email,password)
    print("Successful Sign In!!")
except: 
    print("Invalid user or password! Try again.")

# ============ SIGN UP 
# email = input("Enter your email!")
# password = input("Enter your password!")
# confirm_pass = input("Confirm password!")
# if password == confirm_pass:
#     try:
#         auth.create_user_with_email_and_password(email,password)
#         print("Successful!")
#     except:
#         print("Email already exists!")

# ============================================== Storage

# ================= UPLOAD FILES 
# filename = input("Enter the name if the file you want to upload")
# # difference 
# # which file do i want to upload? THEN what do i want to name it in the cloud? 
# cloudfilename = input("Enter the name of the file on the cloud")
# storage.child(cloudfilename).put(filename)

# print(storage.child(cloudfilename).get_url(None))

# ================= DOWNLOAD FILES 
# cloudfilename = input("Enter the name of the file you want to download")
# # taking the cloudfile name and downloading it into sed file and naming it 
# storage.child(cloudfilename).download("", "downloaded.txt")


# ========================================= DATABASE 
