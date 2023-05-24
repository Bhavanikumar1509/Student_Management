#this file is responsible for sigining ,ecoding,decoding

import time
import jwt
from decouple import config

JWT_SECRET=config("secret")
JWT_ALGORITHM=config("algorithm")

#fucntion return the generaated tokens
def token_response(token:str):
    return{
        "access toke":token
    }
def signJWT(userId:str):
    payload={
        "userId":userId,
        "expiry":time.time()+600
    }
    token=jwt.encode(payload,JWT_SECRET,algorith=JWT_ALGORITHM) # type: ignore
    return token_response(token)
def decodeJWT(token:str):
    try:
        decode_token=jwt.decode(token,JWT_SECRET,algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires']>=time.time() else None
    except:
        return {}
    