import requests
import os

def service_get(service_slug, endpoint, query=None):
   
    service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('stage')}/{service_slug}/{endpoint}"
    
    request = requests.get(service_url, query)

    return request



def service_post(service_slug, endpoint, payload=None):
       
    service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('stage')}/{service_slug}/{endpoint}"
    
    request = requests.post(service_url, data=payload)

    return request
