from fastapi import FastAPI,UploadFile,File,HTTPException
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import shutil
app = FastAPI()


#folder setup
UPLOAD_DIR = Path("upload")               #upload_dir contain the path of upload file.
UPLOAD_DIR.mkdir(exist_ok= True)

#static file
app.mount(                                #this is what it does "Whenever someone requests /uploads/..., go to my uploads folder and serve the requested file."
    "/uploads",
    StaticFiles(directory=UPLOAD_DIR),
    name="uploads"
)

# POST - Upload file
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "url": f"http://127.0.0.1:8000/uploads/{file.filename}"
    }

# GET - Get file

@app.get("/files/{filename}")                
def get_file(filename: str):

    file_path = UPLOAD_DIR / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return {
        "filename": filename,
        "url": f"http://127.0.0.1:8000/uploads/{filename}"
    }
