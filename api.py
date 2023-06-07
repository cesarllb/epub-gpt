from gpt.repo import GptRepo
from upload_epub import process_upload_epub
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import json

app = FastAPI(description='An EPUB document processor designed to enhance your reading experience. With features such as consultation, summarization, explanation, definition, and translation of the book’s text, this tool makes it easy to understand and engage with your favorite books.')
gpt_repo:GptRepo = None

class ReturnBase(BaseModel):
    operation: str
    result: str

@app.post("/upload_epub/")
def upload_epub(file: UploadFile = File(...)) -> str:
    global gpt_repo
    gpt_repo =  process_upload_epub(file)
    return_data = ReturnBase(operation = "epub_gpt.upload_epub", result = "success")
    return return_data.json()

@app.post("/resume/")
def resume(topic:str) -> str:
    data = gpt_repo.resume(topic)
    return_data = ReturnBase(operation = "epub_gpt.resume", result = data)
    return return_data.json()

@app.post("/explain_text/")
def explain_text(text:str) -> str:
    data =  gpt_repo.explain_text(text)
    return_data = ReturnBase(operation = "epub_gpt.explain_text", result = data)
    return return_data.json()


@app.post("/describe_own_name/")
def describe_own_name(noun:str) -> str:
    data = gpt_repo.describe_own_name(noun)
    print(type(data))
    return_data = ReturnBase(operation = "epub_gpt.describe_own_name", result = data)
    return return_data.json()
    
@app.post("/translate_text/")
def translate_text(text:str, language:str) -> str:
    data = gpt_repo.translate_text(text, language)
    return_data = ReturnBase(operation = "epub_gpt.translate_text", result = data)
    return return_data.json()

@app.post("/define_word/")
def define_word(word:str) -> str:
    data = gpt_repo.define_word(word)
    return_data = ReturnBase(operation = "epub_gpt.define_word", result = data)
    return return_data.json()

if __name__ =='__main__':
    import uvicorn
    try:
        uvicorn.run(
                app(), 
                host= '127.0.0.1', 
                port= '8081',
                )
    except Exception as e:
        print(e)