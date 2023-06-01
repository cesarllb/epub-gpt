from fastapi import FastAPI, File, UploadFile
from epub_lib.gpt.repo import GptRepo



app = FastAPI(description='An EPUB document processor designed to enhance your reading experience. With features such as consultation, summarization, explanation, definition, and translation of the book’s text, this tool makes it easy to understand and engage with your favorite books.')
gpt_repo = GptRepo()

@app.get("/")
async def root():
    return {"message": "Hello World"}

async def upload(file: UploadFile = File(...)) -> str:
    proces_upload(file)
    return {"operation": "brainssys.databrain.publisher.upload", "bucket": opp.bucket}

@app.post("/resume")
async def resume(self, topic:str) -> str:
    return self.gpt_repo.resume(topic)

@app.post("/explain_text")
async def explain_text(self, text:str) -> str:
    return self.gpt_repo.explain_text(text)

@app.post("/describe_own_name")
async def describe_own_name(self, noun:str) -> str:
    return self.gpt_repo.describe_own_name(noun)
     
@app.post("/translate_text")
async def translate_text(self, text:str, language:str) -> str:
    return self.gpt_repo.translate_text(text, language)

@app.post("/define_word")
async def define_word(self, word:str) -> str:
    return self.gpt_repo.define_word(word)
