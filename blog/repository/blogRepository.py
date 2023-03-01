import schemas, models
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse
from fastapi import status, HTTPException, Response


# get all blogs
def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        content={'success': False, 'message': f"There are no blogs"}
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=content)
    return blogs


# create blog
def create(request: schemas.Blog, db: Session):
    try:
        new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog
    except IntegrityError as IE:
        return JSONResponse(status_code=500, content={'success': False, 'message': "Duplicate Value"})


# get blog, with specific ID
def show_blog_with_id(id:int, response: Response, db: Session):
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


# delete blog
def destroy(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # if blog doesn't exist
    if not blog:
        content={'success': False, 'message': f"Blog with id {id} does't exist"}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)
    
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()

    content={'success': True, 'message': f"Blog with id {id} deleted"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)


# update blog
def update(id:int, request_body: schemas.Blog, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # If blog doesn't exist
    if not blog:
        content={'success': False, 'message': f"Blog with id {id} doesn't exist"}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)
    
    # exclude_none=True will only update the field which you want to update
    # If you don't want to upadte `body` then pass only `title` and `body` field will stay as it is
    db.query(models.Blog).filter(models.Blog.id == id).update(request_body.dict(exclude_none=True))
    db.commit()

    content={'success': True, 'message': f"Blog with id {id} Updated"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)
