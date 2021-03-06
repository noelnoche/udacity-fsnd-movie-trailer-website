"""
This module sets up server-side caching using `Flask-Cache`.
"""
from flask_caching import Cache


cache_config = {
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}

cache = Cache(config=cache_config)
