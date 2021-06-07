import requests
import os
from .cache import redis_set, redis_hget
import json


def service_get(service_slug, endpoint, headers=None, query=None):

    # retira a barra do endpoint
    if endpoint[0] == '/':
        endpoint = endpoint[1:]
   
    service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('STAGE')}/{service_slug}/{endpoint}"
   
    request = requests.get(service_url, params=query, headers=headers)

    return request


def service_post(service_slug, endpoint, headers=None, payload=None):

    # retira a barra do endpoint
    if endpoint[0] == '/':
        endpoint = endpoint[1:]

    service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('STAGE')}/{service_slug}/{endpoint}"
    
    request = requests.post(service_url, data=payload, headers=headers)

    return request


async def cache_or_service_get(service_slug, endpoint, headers=None, query=None, use_cache=True):

    is_cached = False

    if use_cache:

        cached = await redis_hget(service_slug, endpoint)

        if cached:
            is_cached = True
            request = cached

        else:            
            request = service_get(service_slug, endpoint, headers, query)

    else:
        request = service_get(service_slug, endpoint, headers, query)

    return is_cached, request
