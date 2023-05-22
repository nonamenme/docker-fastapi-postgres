import os
from functools import lru_cache
from pydantic import BaseSettings

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Environment(BaseSettings):
    """ 環境変数を読み込むファイル
    """
    database_url: str

    class Config:
        env_file = os.path.join(PROJECT_ROOT, '.env')

@lru_cache
def get_env():
    """ 「@lru_cache」でディスクから読み込んだ.envの結果をキャッシュする
    """
    return Environment()