import httpx
import os

def service_get(service_slug, endpoint, headers=None, query=None):
   
    service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('STAGE')}/{service_slug}/{endpoint}"
   
    request = httpx.get(service_url, params=query, headers=headers)

    return request


def service_post(service_slug, endpoint, headers=None, payload=None):
       
    service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('STAGE')}/{service_slug}/{endpoint}"
    
    request = httpx.post(service_url, data=payload, headers=headers)

    return request
