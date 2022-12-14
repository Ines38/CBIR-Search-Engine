from typing import Dict, List, Optional
from utils.elasticsearch_functions import ElasticSearch
from fastapi import FastAPI, UploadFile, File
import json
import numpy as np
from PIL import Image
import uvicorn

es = ElasticSearch()

app = FastAPI()

def load_image_into_numpy_array(data):
    return np.array(Image.open(data))

@app.get("/")
async def root():
    return "Welcome To CBIR project"

@app.get("/api/v1/text_query")
async def text_query(query: str, 
                     fields: Optional[str] = '{"tags":1, "Title":2}', 
                     use_fuzzy: Optional[bool] = False,
                     size: Optional[int] = 5, 
                     from_: Optional[int] = 0
                    ):
    
    return es.search_by_text_query(query=query, fields=json.loads(fields), use_fuzzy=use_fuzzy, size=size, from_=from_)

@app.post("/api/v1/image_query")
async def image_query(image_id: Optional[str] = None, 
                      image_link: Optional[str] = None, 
                      image: Optional[UploadFile] = File([]),
                      size: Optional[int] = 5, 
                      from_: Optional[int] = 0,
                      condidates: Optional[int] = 100
                    ):
    x = load_image_into_numpy_array(image.file) if image != [] else np.array([])
    return es.search_by_image_query(image_id=image_id, image_link=image_link, image=x, condidates=condidates, size=size, from_=from_)

@app.post("/api/v1/text_image_query")
async def text_image_query(query: str, 
                      fields: Optional[str] = '{"tags":1, "title":2}', 
                      use_fuzzy: Optional[bool] = False,
                      image_id: Optional[str] = None, 
                      image_link: Optional[str] = None, 
                      image: Optional[UploadFile] = File([]),
                      size: Optional[int] = 5, 
                      from_: Optional[int] = 0,
                      condidates: Optional[int] = 100
                    ):
    x = load_image_into_numpy_array(image.file) if image != [] else np.array([])
    return es.search_by_text_image_query(image_id=image_id, query=query, fields=json.loads(fields), use_fuzzy=use_fuzzy, image_link=image_link, image=x, condidates=condidates, size=size, from_=from_)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)