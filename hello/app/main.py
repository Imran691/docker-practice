from fastapi import FastAPI, Depends
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

ALGORITHM = "HS256"
SECRET_KEY = "A Secure Secret Key"
def create_access_token(subject: str , expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


app : FastAPI = FastAPI()

@app.post("/login")
def login(data_from_user: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)]):
    return {"user_name": data_from_user.username, "password": data_from_user.password}

@app.get("/")
def greet():
    return {"message" : "Hello World"}

@app.get("/who/{who}")
def greet_again(who):
    return f"Hello {who}"

@app.get("/location")
def get_location():
    return {"city" : "Lahore"}

@app.get("/get-token")
def get_token(name:str):
    access_token_expiry = timedelta(minutes=30)
    print(access_token_expiry)
    
    generated_token = create_access_token(subject=name, expires_delta=access_token_expiry)

    return {"access token" : generated_token}


def decode_access_token(access_token: str):
    decoded_jwt = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
    return decoded_jwt

@app.get("/decode_token")
def decoding_token(access_token: str):
    try:
        decoded_token_data = decode_access_token(access_token)
        return {"decoded_token": decoded_token_data}
    except JWTError as e:
        return {"error": str(e)}