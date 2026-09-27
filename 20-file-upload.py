from fastapi import FastAPI,UploadFile,File,HTTPException
from pathlib import Path
app = FastAPI()


#file setup
UPLOAD_DIR = Path("upload")               #upload_dir contain the path of upload file.
UPLOAD_DIR.mkdir(exist_ok= True)
