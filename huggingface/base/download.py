import traceback
from huggingface_hub import snapshot_download

import os

access_token = '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'

def wrapper(repo_id: str, ignore_patterns: list = None, allow_patterns: list = None, cache_dir: str = None):
    try:
        snapshot_download(repo_id=repo_id, ignore_patterns=ignore_patterns, allow_patterns=allow_patterns, cache_dir=cache_dir, resume_download=True, local_dir_use_symlinks=False, token=access_token)
    except:
        traceback.print_exc()
    
# wrapper(repo_id="decapoda-research/llama-7b-hf", ignore_patterns=["*.h5", "*.ot", "*.msgpack"])
wrapper(repo_id="stabilityai/sv3d")
# wrapper(repo_id="lkeab/hq-sam")
