from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from .. import database, oauth2


router = APIRouter(
    prefix="/login",
    tags=['Authentication']
)

@router.post("/", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Invalid Credentials'
        )
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Invalid Credentials'
        )


    # Hash the password
    # hashed_password = utils.hash(user.password)
    # user.password = hashed_password
    # new_user = models.User(**user.model_dump())
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    return {"access_token":access_token, "token_type": "bearer"}