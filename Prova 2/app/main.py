import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Setup logging
logging.basicConfig(filename='app.log', level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

blog_posts = []

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

@app.post("/blog", status_code=201)
async def create_blog_post(post: BlogPost):
    blog_posts.append(post)
    logging.warning(f"Blog post created with id: {post.id}")
    return {"status": "success"}

@app.get("/blog", response_model=List[BlogPost])
async def get_blog_posts():
    return blog_posts

@app.get("/blog/{id}", response_model=BlogPost)
async def get_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            return post
    logging.warning(f"Blog post not found with id: {id}")
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/blog/{id}", status_code=200)
async def delete_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            logging.warning(f"Blog post deleted with id: {id}")
            return {"status": "success"}
    logging.warning(f"Blog post not found for deletion with id: {id}")
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/blog/{id}", status_code=200)
async def update_blog_post(id: int, updated_post: BlogPost):
    for post in blog_posts:
        if post.id == id:
            post.title = updated_post.title
            post.content = updated_post.content
            logging.warning(f"Blog post updated with id: {id}")
            return {"status": "success"}
    logging.warning(f"Blog post not found for update with id: {id}")
    raise HTTPException(status_code=404, detail="Post not found")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
