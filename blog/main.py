from fastapi import FastAPI, Depends, status, Response, HTTPException
from typing import List
import schemas
import models
from hashing import Hash
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse

app = FastAPI()

# It will create the table in database
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Blog
@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db), status_code=status.HTTP_201_CREATED):
    try:
        new_blog = models.Blog(title=request.title, body=request.body)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog
    except IntegrityError as IE:
        return JSONResponse(status_code=500, content={'success': False, 'message': "Duplicate Value"})

# Get all blogs
# for python 3.6 and above -> List[Item]
# for python 3.9 and above -> list[Item]
@app.get('/blog')
def all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    if not blogs:
        content={'success': False, 'message': f"There are no blogs"}
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=content)
    return blogs

# Get a specific ID blog
@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
def show_blog(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # method-1 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} doesn't exist")

        # method-2
        # content = {'success': False, 'message': f"blog with id {id} doesn't exist"}
        # return JSONResponse(status_code=404, content=content)
        
        # method-3
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'success': False, 'message': f"blog with id {id} doesn't exist"}

    return blog

# Delete Blog
@app.delete('/blog/{id}')
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # if blog doesn't exist
    if not blog:
        content={'success': False, 'message': f"Blog with id {id} does't exist"}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)
    
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()

    content={'success': True, 'message': f"Blog with id {id} deleted"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)

# Update Blog
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request_body: schemas.UpdateBlog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # If blog doesn't exist
    if not blog:
        content={'success': False, 'message': f"Blog with idid {id} doesn't exist"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, content=content)
    
    # exclude_none=True will only update the field which you want to update
    # If you don't want to upadte `body` then pass only `title` and `body` field will stay as it is
    db.query(models.Blog).filter(models.Blog.id == id).update(request_body.dict(exclude_none=True))
    db.commit()

    content={'success': True, 'message': f"Blog with id {id} Updated"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)

# Create User
@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user