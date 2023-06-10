import os
import shutil
from pathlib import Path
from fastapi import UploadFile
from setup import config
from tempfile import NamedTemporaryFile
from gpt.repo import GptRepo


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    except shutil.SpecialFileError as e:
        raise e
    except shutil.ReadError as e:
        raise e
    finally:
        upload_file.file.close()
    return tmp_path
    
def process_upload_epub(upload_file: UploadFile) -> GptRepo:
    try:
        tmp_path = save_upload_file_tmp(upload_file)
        db_name = upload_file.filename
        config(tmp_path, db_name)
        gpt_repo = GptRepo()
        try:
            os.remove(tmp_path)
        except OSError as e:
            raise e
        return gpt_repo
    except Exception as e:
        raise e