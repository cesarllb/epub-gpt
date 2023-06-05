from epub_lib.gpt.repo import GptRepo
from upload_epub import process_upload_epub
from fastapi import FastAPI, File, UploadFile

app = FastAPI(description='An EPUB document processor designed to enhance your reading experience. With features such as consultation, summarization, explanation, definition, and translation of the book’s text, this tool makes it easy to understand and engage with your favorite books.')
gpt_repo:GptRepo = None

@app.post("/upload_epub/")
def upload_epub(file: UploadFile = File(...)) -> str:
    global gpt_repo
    gpt_repo =  process_upload_epub(file)
    return 'Success' #{"operation": "epub_gpt.upload_epub", "file_status": "success"}


@app.post("/resume/")
def resume(topic:str) -> str:
    data = gpt_repo.resume(topic)
    return f'"operation": "epub_gpt.resume", "topic": {topic}, "result": {data}'

@app.post("/explain_text/")
def explain_text(text:str) -> str:
    data =  gpt_repo.explain_text(text)
    return f'"operation": "epub_gpt.explain_text", "text": {text}, "result": {data}'


@app.post("/describe_own_name/")
def describe_own_name(noun:str) -> str:
    data = gpt_repo.describe_own_name(noun)
    return f'"operation": "epub_gpt.describe_own_name", "noun": {noun}, "result": {data}'
    
@app.post("/translate_text/")
def translate_text(text:str, language:str) -> str:
    data = gpt_repo.translate_text(text, language)
    return f'"operation": "epub_gpt.translate_text", "text": {text}, "language": {language}, "result": {data}'

@app.post("/define_word/")
def define_word(word:str) -> str:
    data = gpt_repo.define_word(word)
    return f'"operation": "epub_gpt.define_word", "word": {word}, "result": {data}'
