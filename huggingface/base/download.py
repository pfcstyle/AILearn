import traceback
from huggingface_hub import snapshot_download
import os
os.environ['CURL_CA_BUNDLE'] = ''

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:23457/'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:23457/'

def wrapper(repo_id: str, ignore_regex: list = [], allow_patterns: list = []):
    try:
        snapshot_download(repo_id=repo_id, ignore_patterns=ignore_regex, allow_patterns=allow_patterns)
    except:
        traceback.print_exc()
    
wrapper(repo_id="openai/clip-vit-large-patch14", ignore_regex=[], allow_patterns=["*.txt", "*.json"])