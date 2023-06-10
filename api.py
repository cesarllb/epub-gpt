from gpt.repo import GptRepo
from upload_epub import process_upload_epub
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from pydantic import BaseModel


app = FastAPI(description='An EPUB document processor designed to enhance your reading experience. With features such as consultation, summarization, explanation, definition, and translation of the book’s text, this tool makes it easy to understand and engage with your favorite books.')
gpt_repo:GptRepo = None

class ReturnBase(BaseModel):
    operation: str
    result: str

def check_gpt_repo():
    if gpt_repo is None:
        raise HTTPException(status_code=400, detail="upload_epub must be called first")


@app.post("/upload_epub/", description="Upload an EPUB file for processing.")
async def upload_epub(file: UploadFile = File(...)) -> str:
    global gpt_repo
    gpt_repo =  process_upload_epub(file)
    return_data = ReturnBase(operation = "epub_gpt.upload_epub", result = "success")
    return return_data.json()

@app.post("/resume/", description="Generate a summary of the uploaded EPUB file on a given topic.")
async def resume(topic:str, check: None = Depends(check_gpt_repo)) -> str:
    data = gpt_repo.resume(topic)
    return_data = ReturnBase(operation = "epub_gpt.resume", result = data)
    return return_data.json() + topic

@app.post("/explain_text/", description="Provide an explanation of a given text from the uploaded EPUB file.")
async def explain_text(text:str, check: None = Depends(check_gpt_repo)) -> str:
    data =  gpt_repo.explain_text(text)
    return_data = ReturnBase(operation = "epub_gpt.explain_text", result = data)
    return return_data.json()


@app.post("/describe_own_name/", description="Provide a description of a given noun from the uploaded EPUB file.")
async def describe_own_name(noun:str, check: None = Depends(check_gpt_repo)) -> str:
    data = gpt_repo.describe_own_name(noun)
    return_data = ReturnBase(operation = "epub_gpt.describe_own_name", result = data)
    return return_data.json()
    
@app.post("/translate_text/", description= "Translate a given text from the uploaded EPUB file into a specified language.")
async def translate_text(text:str, language:str, check: None = Depends(check_gpt_repo)) -> str:
    data = gpt_repo.translate_text(text, language)
    return_data = ReturnBase(operation = "epub_gpt.translate_text", result = data)
    return return_data.json()

@app.post("/define_word/", description="Provide a definition of a given word from the uploaded EPUB file")
async def define_word(word:str, check: None = Depends(check_gpt_repo)) -> str:
    data = gpt_repo.define_word(word)
    return_data = ReturnBase(operation = "epub_gpt.define_word", result = data)
    return return_data.json()

